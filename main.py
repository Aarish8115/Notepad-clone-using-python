from tkinter import * # imports everything from the tkinter module
from tkinter import filedialog # importing filedialog from tkinter as it is a sub class

# function for saving a file
def save_file():
    file=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if file is None:# if file is not saved after oprning the save as dialogue box this stops the error
        return
    text=str(text_box.get(1.0,END))# gets the text in the textbox for saving
    file.write(text)
    file.close()# closing the file

# for opening an existing file
def open_file():
    file=filedialog.askopenfile(mode="r",filetypes=[("text file","*.txt")])
    if file is not None:# if a file is selected
        content=file.read()
    text_box.delete(1.0,END)# deleting pre existing text in the textbox before opening the file
    text_box.insert(INSERT,content)# inserting text of the opened file in the textbox

root = Tk()# initializing window
root.geometry("800x600")# setting window size
root.title("Notepad Clone by Aarish")# setting the title of the window
root.config(bg="#292926")# background color of the window
root.resizable(False,False)# to make the window non recycleable

# save button
b1=Button(root,width=15,height=1,text="save file",font="varela_round",fg="#292926",bg="white",command=save_file,relief=FLAT).place(x=200,y=15)
# open button
b2=Button(root,width=15,height=1,text="open file",font="varela_round",fg="#292926",bg="white",command=open_file,relief=FLAT).place(x=450,y=15)
# text box
text_box=Text(root,height=28,width=78,bg="white",fg="#292926",font="varela_round",wrap=WORD)
text_box.place(x=50,y=65)

root.mainloop()