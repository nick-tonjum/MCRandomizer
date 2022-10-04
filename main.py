import io
import os
import pathlib
import tkinter
import zipfile
import shutil
from random import choice, random
from tkinter import HORIZONTAL, Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
import tkinter

root = Tk()
root.config(width=200,height=100,bg="#c7dcff")
root.title("MC Randomizer")

randomizeblocks = tkinter.BooleanVar()
randomizeitems = tkinter.BooleanVar()
randomizeblocks.set(value=True)
randomizeitems.set(value=True)

c1 = tkinter.Checkbutton(root,text="Randomize Blocks",variable=randomizeblocks,onvalue=True,offvalue=False,bg="#c7dcff")
c2 = tkinter.Checkbutton(root,text="Randomize Items",variable=randomizeitems,onvalue=True,offvalue=False,bg="#c7dcff")

c1.place(x=25,y=5)
c2.place(x=25,y=25)

donebutton = tkinter.Button(root,text="Randomize!")
donebutton.place(x=55,y=50)

pb = Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
pb.place(x=25,y=80)

successcount = 0
try:
    shutil.rmtree((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace"))))
except Exception as e:
    pass

while successcount == 0:
    packzipfile = askopenfilename()
    if packzipfile[-3:] == "zip":
        successcount = 1
    else:
        tkinter.messagebox.showerror(message="Invalid resource pack file!")
        quit()

with zipfile.ZipFile(pathlib.Path(packzipfile), 'r') as zip_ref:
    try:
        shutil.rmtree((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace"))))
    except Exception as e:
        pass
    os.mkdir((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace"))))
    zip_ref.extractall(pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace")))

if os.path.exists((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/pack.mcmeta")))):
    pass
else:
    try:
        shutil.rmtree((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace"))))
    except Exception as e:
        pass
    tkinter.messagebox.showerror(message="Invalid resource pack file!")
    quit()
    



if randomizeblocks.get():
    blocknames = []
    numberfiles = []
    counter = 0

    filelength1 = len([file for file in os.listdir((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block"))))]) * 2
    pb.config(maximum=filelength1)
    
    for file in os.listdir((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block")))):
        if file[-3:] == "png":
            counter += 1
            blocknames.append(file)
            os.rename((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block/" + file))),(pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block/" + str(counter) + ".png"))))
            numberfiles.append(pathlib.Path("workspace/assets/minecraft/textures/block/" + str(counter) + ".png"))
        pb["value"] += 1
        root.update()
        root.update_idletasks()

    for i in range(1,counter):
        selectedblockname = choice(blocknames)
        os.rename((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block/" + str(i) + ".png"))),(pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/block/" + selectedblockname))))
        pb["value"] += 1
        root.update()
        root.update_idletasks()

if randomizeitems.get():
    itemnames = []
    numberfiles = []
    counter = 0
    filelength2 = len([file for file in os.listdir((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item"))))]) * 2
    for file in os.listdir((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item")))):
        if file[-3:] == "png":
            counter += 1
            itemnames.append(file)
            os.rename((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item/" + file))),(pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item/" + str(counter) + ".png"))))
            numberfiles.append(pathlib.Path("workspace/assets/minecraft/textures/item/" + str(counter) + ".png"))
        pb["value"] += 1
        root.update()
        root.update_idletasks()

    for i in range(1,counter):
        selecteditemname = choice(itemnames)
        os.rename((pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item/" + str(i) + ".png"))),(pathlib.Path.joinpath(pathlib.Path(os.getcwd()),pathlib.Path("workspace/assets/minecraft/textures/item/" + selecteditemname))))
        pb["value"] += 1
        root.update()
        root.update_idletasks()

print("done!")
while True:
    #pb['value'] = 40
    root.update()
    root.update_idletasks()