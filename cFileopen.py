# 新規ライブラリなし
import os
import tkinter.filedialog

# 単一ファイルダイアログ
fTyp = [("", "*")] # ファイルタイプ、拡張子
iDir = os.path.abspath(os.path.dirname(__file__))
file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

print(file_name)

# # 複数ファイルダイアログ
# fTyp = [("", "*")] # ファイルタイプ、拡張子
# iDir = os.path.abspath(os.path.dirname(__file__))
# file_names = tkinter.filedialog.askopenfilenames(filetypes=fTyp, initialdir=iDir)

# print(file_names)
f = open(file_name, 'r', encoding='UTF-8')

data = f.read()

f.close()
print(data)