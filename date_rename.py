#!python3
import os
import sys
import time
import exifread

print ("Current Directory is:", os.getcwd())
cont = input("Rename Files in current directory (Y)es, (N)o\n")
path =  os.getcwd()
if cont in ["Y", "y", "Yes", "yes"]:
    files = os.listdir(path)
    for origName in files:
        if origName.startswith('IMG') and origName.endswith('.CR2'):
            file = open(origName, 'rb')
            tags = exifread.process_file(file)
            createdDate = str(tags.get('EXIF DateTimeOriginal', '0'))
            newName = createdDate.replace(':','_')[0:10] + '_' + origName[4:8] + '.CR2'
            print ("Original Filename is: ", origName)
            print ("Created on: ", createdDate)
            print ("New Name: ", newName)
            file.close()
            os.rename(origName, newName)
            time.sleep(.25)
        else:
            print ("Skipping: ", origName)
            time.sleep(.05)
            pass
else: 
    quit()
