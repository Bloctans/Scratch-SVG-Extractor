import tkinter as tk
from tkinter import filedialog
import zipfile
import json
import shutil
import os
print("imported libarys")

folder = './extracted'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

folder = './sprites'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

root = tk.Tk()
root.withdraw()

filetypes = (
        ('SB3 files', '*.sb3'),
        ('ZIP files', '*.zip')
    )

file_path = filedialog.askopenfilename(filetypes=filetypes)
if file_path == "":
    print("File Path was blank")
    quit()

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall('./extracted')

json_data = open("./extracted/project.json", 'r',  encoding='utf-8').read()
  
obj = json.loads(json_data)

for sprite in obj["targets"]:
    for costume in sprite["costumes"]:
        if costume["dataFormat"] == "svg":
            try:
                if not os.path.exists("./sprites/"+sprite["name"]+"/"):
                    os.makedirs("./sprites/"+sprite["name"]+"/")
                tocopy = open("./extracted/"+costume["md5ext"], "r", encoding='utf-8').read()
                writeto = open("./sprites/"+sprite["name"]+"/"+costume["name"]+"."+costume["dataFormat"], "w")
                writeto.write(tocopy)
                print("sucessfully extracted " + "./extracted/"+costume["md5ext"] + " to " + "./sprites/"+sprite["name"]+"/"+costume["name"]+"."+costume["dataFormat"])
            except:
                print("error with ./sprites/"+sprite["name"]+"/"+costume["name"]+"."+costume["dataFormat"])
        else:
            print("./sprites/"+sprite["name"]+"/"+costume["name"]+"."+costume["dataFormat"] + " isnt an SVG")

print("Cleaning up...")

folder = './extracted'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

input("File done.")
