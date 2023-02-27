from tkinter import *;
import backend as b

window= Tk();
window.title("Girlfriend/Crush Database")
window.geometry("600x200")


try:
    window.iconbitmap("gift/icon.ico")
except:
    window.iconbitmap("icon.ico")
window.resizable(width=False,height=False)
title_main = Label(window, text="Girlfriend/Crush Database", font=("Arial", 40));
# title_main2 = Label(window, text="HAPPY BIRTHDAY BRUV!!", font=("Arial", 20));
frame = Frame(window,bg="green")
add = Button(frame,text="ADD",font=("Arial", 20),command=lambda:b.add())
remove = Button(frame,text="REMOVE",font=("Arial", 20),command=lambda:b.remove())
seeall = Button(frame,text="SEE ALL",font=("Arial",20),command=lambda:b.see_all())

if __name__ == "__main__":
    title_main.pack()
    add.pack(side=LEFT)
    remove.pack(side=RIGHT)
    seeall.pack()
    frame.pack(padx=30,pady=20)
    title_main2.pack()
    window.mainloop()