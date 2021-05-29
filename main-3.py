from tkinter import *
from tkinter import messagebox

#window
root = Tk()
root.geometry('500x500')
root.title('Login Form')
root.config(bg="aqua")

#username label and text entry box
usernameLabel = Label(root, text="Please enter username:")
usernameLabel.place(x=5, y=5)

usernameEntry = Entry(root)
usernameEntry.place(x=100, y=5)


#password label and password entry box
passwordLabel = Label(root,text="Please enter password:")
passwordLabel.place(x=5, y=50)


passwordEntry = Entry(root,  show='*')
passwordEntry.place(x=100, y=50)

def membership():
    names = ["Zoe","Lihle","Liyaah","Masi"]
    passwords = ["9621","5462","5412","8956"]
    found=False
    for x in range(len(names)):
        if usernameEntry.get()==names[x] and passwordEntry.get()==passwords[x]:
            found=True
    if found==True:
        messagebox.showinfo("ACCESS INFO", "ACCESS GRANTED")
    else:
        messagebox.showinfo("ACCESS INFO", "ACCESS DENIED")


def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)


def exit():
    return root.destroy()


#login button
loginButton = Button(root, text="Login",command=membership)
loginButton.place(x=100, y=100)

#clear button
clear_btn = Button(root, text="Clear",command=clear)
clear_btn.place(x=200, y=100)

#exit button
exit_btn = Button(root, text="Exit",command=exit)
exit_btn.place(x=300, y=100)

root.mainloop()
