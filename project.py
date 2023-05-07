import os
import shutil
fromdir = "C:/Users/ishan/Downloads" 
todir = "C:/Users/ishan/Pictures/Saved Pictures"

listoffiles = os.listdir(fromdir)
#print(listoffiles)

for filename in listoffiles:
    name, ext = os.path.splitext(filename)
    #print(name)
    #print(ext)

    if ext=="":
        continue
    if ext in [".txt", ".pdf", ".doc", ".docx"]:
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "documentfiles"
        path3 = todir + "/" + "documentfiles" + "/" + filename
        print(path1)
        print(path2)
        print(path3)
        if os.path.exists(path2):
            print("moving", filename)
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("moving", filename)
            shutil.move(path1,path3)