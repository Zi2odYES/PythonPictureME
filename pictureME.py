#                  
from tkinter import*
from PIL import Image
from PIL import ImageTk
import os
win = Tk()
#    标题
win.title('PythonPictureME')
os.listdir()
N = 1
# 按钮函数
def Last():
    global N
    N -= 1
    if N == 0:
        N = 3
    img_New = Image.open(str(N)+'.jpg')
    img_New = ImageTk.PhotoImage(img_New)
    # 更改图片
    ph.configure(image=img_New)
    ph.image = img_New
def Next():
    global N
    N += 1
    if N > 3:
        N = 1
    img_New = Image.open(str(N)+'.jpg')
    img_New = ImageTk.PhotoImage(img_New)
    # 更改图片
    ph.configure(image=img_New)
    ph.image = img_New

img = Image.open(str(N)+'.jpg')
img = ImageTk.PhotoImage(img)
ph = Label(win, image=img)
ph.grid(row=1, column=1)

# 上一张
bottom1 = Button(win, text='Last', font=('AGENCYR', 30),command=Last)
bottom1.grid(row=0, column=0)
# 下一张
bottom2 = Button(win, text='Next', font=('AGENCYR', 30),command=Next)
bottom2.grid(row=0, column=1)

mainloop()
