from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("My Calculator")
screen.configure(bg="powder blue")
screen.iconbitmap('cal.ico')
screen.maxsize(width=453,height=486)
screen.minsize(width=350,height=486)

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)
def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result= eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo("Notification",'try again something is wrong here',parent=screen)

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", 'try again something is wrong here', parent=screen)
def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", 'try again something is wrong here', parent=screen)
def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", 'try again something is wrong here', parent=screen)

def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", 'try again something is wrong here', parent=screen)

def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", 'try again something is wrong here', parent=screen)




tex = StringVar()
operator = ''
entry1=Entry(screen,bg='orange',font=('arial',20,'italic bold'),bd='25',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
AllButton=()
btn7=Button(screen,text='7',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),activebackground = 'yellow',activeforeground = 'white')
btn7.grid(row=1,column=0)
btn8=Button(screen,text='8',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground = 'yellow',activeforeground = 'white')
btn8.grid(row=1,column=1)
btn9=Button(screen,text='9',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground = 'yellow',activeforeground = 'white')
btn9.grid(row=1,column=2)
btnadd=Button(screen,text='+',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),activebackground = 'yellow',activeforeground = 'white')
btnadd.grid(row=1,column=3)
btn4=Button(screen,text='4',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground = 'yellow',activeforeground = 'white')
btn4.grid(row=2,column=0)
btn5=Button(screen,text='5',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground = 'yellow',activeforeground = 'white')
btn5.grid(row=2,column=1)
btn6=Button(screen,text='6',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground = 'yellow',activeforeground = 'white')
btn6.grid(row=2,column=2)
btnsub=Button(screen,text='-',font=('arial','20','italic bold'),bd=8,padx=18,pady=16,command=lambda:click('-'),activebackground = 'yellow',activeforeground = 'white')
btnsub.grid(row=2,column=3)
btn1=Button(screen,text='1',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground = 'yellow',activeforeground = 'white')
btn1.grid(row=3,column=0)
btn2=Button(screen,text='2',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground = 'yellow',activeforeground = 'white')
btn2.grid(row=3,column=1)
btn3=Button(screen,text='3',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground = 'yellow',activeforeground = 'white')
btn3.grid(row=3,column=2)
btnmul=Button(screen,text='*',font=('arial','20','italic bold'),bd=8,padx=18,pady=16,command=lambda:click('*'),activebackground = 'yellow',activeforeground = 'white')
btnmul.grid(row=3,column=3)
btn0=Button(screen,text='0',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground = 'yellow',activeforeground = 'white')
btn0.grid(row=4,column=0)
btnclear=Button(screen,text='C',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground = 'yellow',activeforeground = 'white')
btnclear.grid(row=4,column=1)
btnequal=Button(screen,text='=',font=('arial','20','italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground = 'yellow',activeforeground = 'white')
btnequal.grid(row=4,column=2)
btndiv=Button(screen,text='/',font=('arial','20','italic bold'),bd=8,padx=18,pady=16,command=lambda:click('/'),activebackground = 'yellow',activeforeground = 'white')
btndiv.grid(row=4,column=3)

####################################### Advance Calculation###############################################
btnsin=Button(screen,text='sin',font=('arial','15','italic bold'),bd=8,padx=15,pady=19,command=cmsin,activebackground = 'yellow',activeforeground = 'white')
btnsin.grid(row=0,column=4)
btncos=Button(screen,text='cos',font=('arial','15','italic bold'),bd=8,padx=15,pady=19,command=cmcos,activebackground = 'yellow',activeforeground = 'white')
btncos.grid(row=1,column=4)
btntan=Button(screen,text='tan',font=('arial','15','italic bold'),bd=8,padx=16,pady=19,command=cmtan,activebackground = 'yellow',activeforeground = 'white')
btntan.grid(row=2,column=4)
btnsqr=Button(screen,text='sqr',font=('arial','15','italic bold'),bd=8,padx=15,pady=19,command=cmsqrt,activebackground = 'yellow',activeforeground = 'white')
btnsqr.grid(row=3,column=4)
btnlog=Button(screen,text='log',font=('arial','15','italic bold'),bd=8,padx=16,pady=19,command=cmlog,activebackground = 'yellow',activeforeground = 'white')
btnlog.grid(row=4,column=4)
screen.mainloop()