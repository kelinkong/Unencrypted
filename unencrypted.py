import tkinter
from tkinter import filedialog
import pikepdf
import os

print('请选择PDF文件。 Please choose PDF.\n')

# 打开一个文件选择对话框
root = tkinter.Tk()
root.withdraw() # 隐藏多余的窗口

# 选择文件路径
filePath = filedialog.askopenfilename()

import os

# 用pikepdf破解
pdf = pikepdf.open(filePath)

# 获取文件的路径和名称
dir_name = os.path.dirname(filePath)
base_name = os.path.basename(filePath)

# 在原路径下保存解锁的 PDF 文件，并使用原文件名
unlocked_file_path = os.path.join(dir_name, 'unlocked_' + base_name)
pdf.save(unlocked_file_path)

print('解密完成。 Unloked done.')