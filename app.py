from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()  # object creation for tkinter


def login_cred():
    print('Details:')
    email1 = email_input.get()
    pwd1 = pwd_input.get()
    print('Email:', email1)
    print('Password:', pwd1)
    if email1 == 'rashikadabas2000@gmail.com' and pwd1 == '1234':
        messagebox.showinfo('Done', 'Login Successfully')
    else:
        messagebox.showerror('Error', 'Login Failed')


root.title('Minerskape')
root.iconbitmap('favicon.ico')
root.minsize(200, 100)
root.maxsize(300, 450)
root.geometry('300x450')  # default size for GUI when opening
root.configure(background='#2c3696')

img = Image.open('miners.png')
img_size = img.resize((60, 60))
img = ImageTk.PhotoImage(img_size)
img_label = Label(root, image=img, bg='#2c3696')
img_label.pack(pady=(10, 10))

text_m = Label(root, text='Minerskape', fg='white', bg='#2c3696')
text_m.pack()
text_m.configure(font=('verdana', 20))

email = Label(root, text='Enter Email:', fg='white', bg='#2c3696')
email.pack(pady=(20, 5))
email.configure(font=('verdana', 11))

email_input = Entry(root, width=40)
email_input.pack(ipady=4, pady=(1, 15))

pwd = Label(root, text='Enter Password:', fg='white', bg='#2c3696')
pwd.pack(pady=(20, 5))
pwd.configure(font=('verdana', 11))

pwd_input = Entry(root, width=40)
pwd_input.pack(ipady=4, pady=(1, 15))

login_btn = Button(root, text='Login', bg='white', fg='black', width=10, command=login_cred)
login_btn.pack(pady=(10, 10))
login_btn.configure(font=('verdana', 11))


root.mainloop()  # to run GUI
