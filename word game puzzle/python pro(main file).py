import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import sqlite3 
import time


def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('WORD GAME Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Word Game Login",fg="white",bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                messagebox.showinfo("WELCOME","Best of Luck")
                import project
                
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Word Game')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="GAME SignUp",fg="brown",bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('word game.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('word game.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()
def start():
    global root 
    root = Tk()
    root.title('Welcome To Word puzzle game App')
    canvas = Canvas(root,width = 600,height = 440, bg = 'orange')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="cover.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage,bg="red",fg="black") 
    button.configure(width = 84,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
if __name__=='__main__':
    start()
