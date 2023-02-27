from tkinter import *
from main import *
import pymongo
import dotenv



client = pymongo.MongoClient(dotenv.get_key(key_to_get="TOKEN",dotenv_path=".env"))
db = client["main"].get_collection("data")


def add():
    root = Tk()
    root.title("Add Girlfriend/Crush")
    root.iconbitmap("icon.ico")
    title = Label(root,text="Type the name: (Press enter and the name is saved)")
    name_entry = Entry(root,width=80)
    enter= Button(root,text="Enter",command=lambda:db.insert_one({"Name":name_entry.get()}))
    title.pack()
    name_entry.pack()
    enter.pack()
    root.mainloop()

def remove():
    root = Tk()
    root.iconbitmap("icon.ico")
    root.title("Remove Girlfriend/Crush")
    title = Label(root,text="Type the name: (Press enter and the name is deleted)")
    name_entry = Entry(root,width=80)
    enter= Button(root,text="Enter",command=lambda:db.find_one_and_delete({"Name":name_entry.get()}))
    title.pack()
    name_entry.pack()
    enter.pack()
    root.mainloop()

def see_all():
    root=Tk()
    root.iconbitmap("icon.ico")
    root.title("list")
    list = Listbox(root)
    i=1
    for x in db.find():
        list.insert(i,x.get("Name"))
        i+=1
    list.pack()
    root.mainloop()






    
    
