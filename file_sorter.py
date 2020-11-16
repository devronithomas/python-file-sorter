#importing libraries
import os
import shutil

#function to move files and make respective dir
def mv_file(file_name):
    #choose folder name depending on type of file
    if file_name == docs:
        dir_name = "Documents"
    elif file_name == img:
        dir_name = "Images"
    elif file_name == prg:
        dir_name = "Programs"
    elif file_name == comprs:
        dir_name = "Compressed"
    elif file_name == aud:
        dir_name = "Audio"
    elif file_name == vid:
        dir_name = "Video"

    try:
        os.mkdir(root + f"/{dir_name}")
        print (f"Creating dir to store {dir_name}")
        print (f"***{dir_name} path:",root + f"/{dir_name}")
        shutil.move(sort_dir + "/" + files, root + f"/{dir_name}")
        print (f"{files} moved to {dir_name}")
    except:
        shutil.move(sort_dir + "/" + files, root + f"/{dir_name}")
        print (f"{files} moved to {dir_name}")

#create a sorting folder
root = os.path.dirname(__file__)
try:
    os.mkdir(root + "/Sorting Folder")
    print ('Creating Sorting folder')
except:
    pass

#above made folder dir location
sort_dir = root + "/Sorting Folder"
print (f"""Sorting folder dir: {sort_dir}
***Move files into this folder to sort***""")

input("Press Enter once files are ready to sort")

#file types
docs = (".docx", ".doc", ".pdf", ".txt")
img = (".png", ".jpeg", ".jpg")
prg = (".exe", ".msi")
comprs = (".zip", ".rar")
aud = (".mp3", ".wav")
vid = (".mp4", ".mov", ".avi")

if len(os.listdir(sort_dir)) > 0:
    #calling above move file function
    for files in os.listdir(sort_dir):
        if files.endswith(docs):
            mv_file(docs)
        elif files.endswith(img):
            mv_file(img)
        elif files.endswith(prg):
            mv_file(prg)
        elif files.endswith(comprs):
            mv_file(comprs)
        elif files.endswith(aud):
            mv_file(aud)
        elif files.endswith(vid):
            mv_file(vid)
        else:
            print(f"Unsupported file extension {files.split('.')[1]}")
            
    print("All files are sorted")
else:
    print ("No Files to Sort")