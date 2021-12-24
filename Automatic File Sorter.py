import os

def fileSorter(file, extension):
    """ 
    Changes file's path from current folder to a more suitable one dependent on its extension.

    :param str file: File's path
    :param str extension: File's extension
    :return: File's updated path
    """
    file_path = file.split("\\")
    videos = ["mp4", "mov", "wmv", "flv", "avi", "webm", "mkv"]
    documents = ["pdf", "doc", "docx", "odt", "txt", "rtf", "ppt", "pptx", "odp"]
    pictures = ["jpg", "jpeg", "png", "gif", "webp", "tiff", "psd", "raw", "bmp", "heif", "indd", "svg"]
    music = ["pcm", "wav", "mp3", "aiff", "aac", "ogg", "wma", "flac", "alac"]

    if (extension in documents):
        file_path[3] = "Documents"
    elif (extension in videos):
        file_path[3] = "Videos"
    elif (extension in pictures):
        file_path[3] = "Pictures"
    elif (extension in music):
        file_path[3] = "Music"
    else:
        file_path[3] = "Downloads"
    return  ("\\".join(file_path))

def extensionFinder(file):
    """
    Gets a file's extension
    :param str file: File's path
    :return: File's extension
    """
    file = file.split("\\")
    file = file[4]
    extension = ""
    for i in file:
        extension += i
        if (i == "."):
            extension = ""
    return extension

def filePathFinder(folderPath):
    fileList = os.listdir(folderPath)
    new_list = []
    for i in fileList:
        new_list.append(folderPath + "\\" + i)
    return (new_list)
    
        

def indivdual():
    """
    Relocates an indivdual file into a more suitable folder
    """
    while (True):
        try:
            file = str(input("Enter file path: "))
            extension = extensionFinder(file)
            new_file = fileSorter(file, extension)
            os.rename(file, new_file)
        except FileNotFoundError:
            answer = str(input("File not found. Would you like to try another file? ")).lower()
            if (answer == "yes"):
                indivdual()
            else:
                break

def multi():
    """
    Relocates all of a folder's contents into more suitable folders
    """
    while (True):
        try:
            folderPath = str(input("Enter folder path: "))
            fileList = filePathFinder(folderPath)
            for i in fileList:
                extension = extensionFinder(i)
                new_file = fileSorter(i , extension)
                os.rename(i, new_file)
        except FileNotFoundError:
            answer = str(input("File not found. Would you like to try another file? ")).lower()
            if (answer == "yes"):
                multi()
            else:
                break
    
def main():
    """
    Main function
    """
    prompt = str(input("Would you like to relocate an individual file or and entire folders contents? (single/multiple): "))
    if (prompt.lower() == "single"):
        indivdual()
    elif (prompt.lower() == "multiple"):
        multi()
    else:
        main()

main()
