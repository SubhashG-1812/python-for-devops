import os
folder = input("Enter the folder names with spaces")
folder.split
for folders in folder:
    files = os.listdir(folders)
    print(files)
