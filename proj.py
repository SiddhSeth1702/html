import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image 
from PIL import ImageTk 
from tkinter import ttk


root=Tk()
root.title('Log In')
root.geometry('925x500+300+200')
root.configure(bg='#041C32')
root.resizable(False,False)
def key_bind(e):
        show()
def focus(event):
    user.focus_set()
    event.widget.tk_focusPrev().focus()
    return("break")
def focus_n(event):
    event.widget.tk_focusNext().focus()
    return("break")

def connectdb(hostname,username,password):
        try:
            conn = None
            conn = mysql.connector.connect(
                host=hostname,
                user=username,
                passwd=password
            )
            #print("database connectivity successfully......")
            return conn
        except Error as f:
            print(f"Error : {f}")
def q_exe(conn,query):
        try:
            cur1=conn.cursor()
            cur1.execute(query)
        except Error as f:
            print(f"Error : {f}")
def fetch(conn,query):
    try:
        mycursor = conn.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    except Error as f:
        print(f"Error:{f}")
def q_insert(conn,query):
    try:
        cur1=conn.cursor()
        cur1.execute(query)
        print("Data inserted successfully.......")
        conn.commit()
        conn.close()
    except Error as f:
        print(f"Error : {f}")
def entry():
    username=user.get()
    password=user1.get()
    conpass=user2.get()
    unm=str(username)# converting stringvar() to string 
    psw=str(password)
    conn=connectdb("localhost","root","Siddh@1310") #connecting to database(database is already created in sql)
    q_exe(conn,"use admn;")#use databasename
    q3=("""Select user_name from cred;""") #query for displaying only username from table
    val=(fetch(conn,q3))#fetching username from table as a list(table is already created in sql)
    flag=0
    #checking if username already exist
    if password==conpass:
        for i in range(len(val)):
            if username==val[i][0]:
                flag=1
        if flag==1:
            resp=mb.showwarning("Abort","User already exist")
        else:
            q2=(f"Insert into cred (user_name,user_password) values ('{unm}','{psw}');")
            q_insert(conn,q2)
            resp=mb.showinfo("Login Info",f"Sign UP Succesfull")

def show():
    username=user.get()
    password=user1.get()
    conn=connectdb("localhost","root","Siddh@1310")
    q_exe(conn,"use admn")
    q2=(f"""Select user_name,user_password from cred;""")
    val=fetch(conn,q2)
    flag=0
    for i in range(len(val)):
        if username==val[i][0] and password==val[i][1]:
            flag=1
    if flag==1:
        resp=mb.showinfo("Login Info",f"User {username.title()} has been login")
    else:
        resp=mb.showwarning("Abort","Invalid credentials")
def signup():
    frame.destroy()
    sigupframe()

def sigupframe():
    frame=Frame(root,width=350,height=350,bg='white')
    frame.place(x=545,y=70)

    heading=Label(frame,text='Sign Up',fg='#1e90ff',bg='white',font=('Microsoft yahei UI Light',23,'bold'))
    heading.place(x=115,y=5)

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    global user;
    user = Entry(frame,width=25,fg='#041C32',border=0,bg='white',font=('Microsoft yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='#041C32').place(x=25,y=107)


    def on_enter(e):
        user1.delete(0,'end')
    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,'Password')
    user1 = Entry(frame,width=25,fg='#041C32',border=0,bg='white',font=('Microsoft yahei UI Light',11))
    user1.place(x=30,y=150)
    user1.insert(0,'Password')
    user1.bind('<FocusIn>',on_enter)
    user1.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='#041C32').place(x=25,y=177)

    ##################################
    global user2;
    def on_enter(e):
        user2.delete(0,'end')
    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Confirm Password')
    root.bind("<Up>",focus)
    root.bind("<Down>",focus_n)
    
    
    
    user2 = Entry(frame,width=25,fg='#041C32',border=0,bg='white',font=('Microsoft yahei UI Light',11))
    user2.place(x=30,y=215)
    user2.insert(0,' Confirm Password')
    user2.bind('<FocusIn>',on_enter)
    user2.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='#041C32').place(x=25,y=237)
    Button(frame,width=39,pady=7,text="Sign Up",bg='#1e90ff',fg='white',border=0,command=entry,cursor='hand2').place(x=35,y=264)
    label=Label(frame,text="Account Already exist?",fg="black",bg='white',font=('Microsoft yahei UI Light',9))
    label.place(x=70,y=310)
    sign_up=Button(frame,width=4,text='Sign in',command=login,border=0,bg='white',cursor='hand2',fg="#1e90ff")
    sign_up.place(x=215,y=310)



 
img=ImageTk.PhotoImage(Image.open(r"C:\Users\Siddh Seth\Desktop\4826435.png"))
Label(root,image=img,bg='#041C32').place(x=2,y=2)
def login():
    global frame;
    frame =Frame(root,width=350,height=350,bg='white')
    frame.place(x=545,y=70)

    heading=Label(frame,text='Sign In',fg='#1e90ff',bg='white',font=('Microsoft yahei UI Light',23,'bold'))
    heading.place(x=115,y=5)

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    global user;
    user = Entry(frame,width=25,fg='#041C32',border=0,bg='white',font=('Microsoft yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='#041C32').place(x=25,y=107)
    root.bind("<Up>",focus)
    root.bind("<Down>",focus_n)


    def on_enter(e):
        user1.delete(0,'end')
    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,'Password')
   
    global user1;
    user1 = Entry(frame,width=25,fg='#041C32',border=0,bg='white',font=('Microsoft yahei UI Light',11))
    user1.place(x=30,y=150)
    user1.insert(0,'Password')
    user1.bind('<FocusIn>',on_enter)
    user1.bind('<FocusOut>',on_leave)  

    Frame(frame,width=295,height=2,bg='#041C32').place(x=25,y=177)

    Button(frame,width=39,pady=7,text="Sign In",bg='#1e90ff',fg='white',border=0,command=show,cursor='hand2').place(x=35,y=204)
    root.bind("<Return>",key_bind)
    label=Label(frame,text="Don't have an account?",fg="black",bg='white',font=('Microsoft yahei UI Light',9))
    label.place(x=75,y=270)
    sign_up=Button(frame,width=6,text='Sign Up',command=signup,border=0,bg='white',cursor='hand2',fg="#1e90ff")
    sign_up.place(x=215,y=270)
login()
root.mainloop()
##############################################################


    