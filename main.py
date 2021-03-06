from tkinter import *
from tkinter import messagebox

# The info for the window
window = Tk()
window.title("Verify Form")
window.geometry("540x340")
window.resizable(False, False)

user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
             'Yamkela': 'breadislife'}

entry1 = Label(window, text="Username")
entry1.place(x=50, y=50)
entry1 = Entry(window)
entry1.place(x=200, y=50)
entry2 = Label(window, text="Password")
entry2.place(x=50, y=100)
entry2 = Entry(window)
entry2.place(x=200, y=100)


def verification():
    username = entry1.get()
    password = entry2.get()

    if username in user_pass:
        pw = user_pass.get(username)
        if pw == password:
            window.destroy()
            import main2
        else:
            messagebox.showerror(message="Username and password does not match")
    else:
        messagebox.showerror(message="Username does not exist")


def delete():
    entry1.delete(0, 'end')
    entry2.config(state="normal")
    entry2.delete(0, END)

verify = Button(window, text="verify", width=15, command=verification).place(x=50, y=200)
clear = Button(window, text="Clear", width=15, command=delete).place(x=200, y=200)
quit = Button(window, text="Exit", width=15, command="exit").place(x=350, y=200)

window.mainloop()
