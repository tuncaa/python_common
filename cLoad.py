import os
import tkinter.filedialog

def FileOpenDialog(fTyp = [("", "*")],iDir = os.path.abspath(os.path.dirname(__file__))):

    file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    return file_name
