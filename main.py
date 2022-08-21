from tkinter import *
from tkinter import filedialog

def save_file():
    file=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if file is None:
        return
    text=str(text_box.get(1.0,END))
    file.write(text)
    file.close()

def open_file():
    file=filedialog.askopenfile(mode="r",filetypes=[("text file","*.txt")])
    if file is not None:
        content=file.read()
    text_box.delete(1.0,END)
    text_box.insert(INSERT,content)

root = Tk()
root.geometry("800x600")
root.title("Notepad Clone by Aarish")
root.config(bg="#292926")
root.resizable(False,False)

b1=Button(root,width=15,height=1,text="save file",font="varela_round",fg="#292926",bg="white",command=save_file).place(x=200,y=15)
b2=Button(root,width=15,height=1,text="open file",font="varela_round",fg="#292926",bg="white",command=open_file).place(x=450,y=15)
text_box=Text(root,height=28,width=78,bg="white",fg="#292926",font="varela_round",wrap=WORD)
text_box.place(x=50,y=65)

root.mainloop()