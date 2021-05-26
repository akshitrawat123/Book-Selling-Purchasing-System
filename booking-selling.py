from tkinter import *
import tkinter.messagebox as tmsg
def n():
    tmsg.showinfo("display books","c++- the foundation at price-->Rs799 only")
def m():
    tmsg.showinfo("display books","java- welcome to java at price--> Rs699 only")
def e():
    tmsg.showinfo("display books","python-the beginner's book at price-->Rs649 only" )
def w():
    tmsg.showinfo("display books","let us c at price-->Rs549")
def s():
    tmsg.showinfo("diaplay books","jvascript-expert in language at price Rs-->Rs599 only")
def u():
    tmsg.showinfo("display books","ruby on rails!! at price-->Rs599 only")
def l():
    tmsg.showinfo("display books","django--the web developement master at price-->Rs699 only")
def h():
    tmsg.showinfo("display books","kotlin-welcome to android development at price-->Rs999 only")
def c():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy c++")
def j():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy java" )
def p():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy python")
def cc():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy c")
def jj():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy javascript")
def r():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy ruby")
def dj():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy django")
def ko():
    tmsg.showinfo("Buy books","Hey! you hava successfully Buy kotlin")
def nw():
    tmsg.showinfo("Sell book","Hey! your request to sell book has approved!")
def mw():
    tmsg.showinfo("sell book","Hey! your request to sell book has approved!")
def ew():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")
def ww():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")
def sw():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")
def uw():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")
def lw():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")
def hw():
    tmsg.showinfo("sell book", "Hey! your request to sell book has approved!")


def display():
    root=Tk()
    root.title('display book')
    root.geometry('488x466')
    Button(root,text="c++",width=30,height=2,command=n).pack()
    Button(root, text="java", width=30,height=2,command=m).pack()
    Button(root, text="python", width=30,height=2,command=e).pack()
    Button(root, text="c", width=30,height=2,command=w).pack()
    Button(root, text="javascript", width=30,height=2,command=s).pack()
    Button(root, text="ruby", width=30,height=2,command=u).pack()
    Button(root, text="django", width=30,height=2,command=l).pack()
    Button(root, text="kotlin", width=30,height=2,command=h).pack()


def sell():
    root=Tk()
    root.title('Sell book')
    tmsg.askquestion("Sell book","do you want to sell book??")
    Label(root,text="click the book you want to get??")
    Button(root, text="c++ at price-->Rs799 only", width=30, height=2, command=nw).pack()
    Button(root, text="java at price-->Rs699 only", width=30, height=2, command=mw).pack()
    Button(root, text="python at price-->Rs649 only", width=30, height=2, command=ew).pack()
    Button(root, text="c at price-->Rs549 only", width=30, height=2, command=ww).pack()
    Button(root, text="javascript at price-->Rs599 only", width=30, height=2, command=sw).pack()
    Button(root, text="ruby at price-->Rs599 only", width=30, height=2, command=uw).pack()
    Button(root, text="django at price-->Rs699 only", width=30, height=2, command=lw).pack()
    Button(root, text="kotlin at price-->999 only", width=30, height=2, command=hw).pack()
    root.geometry('490x490')

def Buy():
    root=Tk()
    root.title('Buy book')
    root.geometry('488x466')
    Button(root, text="c++", width=30, height=2, command=c).pack()
    Button(root, text="java", width=30, height=2, command=j).pack()
    Button(root, text="python", width=30, height=2, command=p).pack()
    Button(root, text="c", width=30, height=2, command=cc).pack()
    Button(root, text="javascript", width=30, height=2, command=jj).pack()
    Button(root, text="ruby", width=30, height=2, command=r).pack()
    Button(root, text="django", width=30, height=2, command=dj).pack()
    Button(root, text="kotlin", width=30, height=2, command=ko).pack()
def submit():
    tmsg.showinfo("Sumbit form","Hey!! thanks for sharing your details")
    binfo=bval.get()
    cinfo=cval.get()
    dinfo=dval.get()
    einfo=eval.get()
    finfo=fval.get()
    print("your name is"+bval.get())
    print("your age is "+cval.get())
    print("Book name is"+dval.get())
    print("mobile number is"+eval.get())
    print("your email id is"+fval.get())
    file=open("book.txt","w")
    file.write("your name is"+binfo)
    file.write("\n")
    file.write("your age is "+cinfo)
    file.write("\n")
    file.write("Book name is"+dinfo)
    file.write("\n")
    file.write("mobile number is"+einfo)
    file.write("\n")
    file.write("your email id is"+finfo)

root=Tk()
root.title('Sales management system for  used books')
root.geometry("888x566")
a=Label(root,text="You can fill your details here",font="lucida 18 bold").grid(row=0,column=3)
bval=StringVar()
cval=StringVar()
dval=StringVar()
eval=StringVar()
fval=StringVar()
b=Label(root,text="Enter Your Name",bg="yellow",fg="black")
c=Label(root,text="Enter your Age",bg="red",fg="black")
d=Label(root,text="Enter book name",bg="grey",fg="black")
e=Label(root,text="Enter your mobile number",fg="blue",bg="grey")
f=Label(root,text="Enter your email id",fg="green",bg="grey")
b.grid(row=2,column=2)
c.grid(row=3,column=2)
d.grid(row=4,column=2)
e.grid(row=5,column=2)
f.grid(row=6,column=2)
bentry=Entry(root,textvariable=bval).grid(row=2,column=3)
centry=Entry(root,textvariable=cval).grid(row=3,column=3)
dentry=Entry(root,textvariable=dval).grid(row=4,column=3)
eentry=Entry(root,textvariable=eval).grid(row=5,column=3)
fentry=Entry(root,textvariable=fval).grid(row=6,column=3)
Button(text="submit",command=submit,bg="red",fg="black").grid(row=7,column=3)

Button(root,text="display books",width=40,height=5,command=display,fg="black",bg="yellow").grid(row=9,column=2)
Button(root,text="sale book",width=40,height=5,command=sell).grid(row=10,column=2)

Button(root,text="Buy book",width=40,height=5,command=Buy).grid(row=11,column=2)

root.mainloop()