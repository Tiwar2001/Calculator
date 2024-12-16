from tkinter import *
import math  

win = Tk()
win.title('100-MS')
win.geometry('400x400')
win.configure(bg='lightgrey')
e = Entry(win, width=56, borderwidth=15,bg='grey',fg='black')
e.place(x=0, y=0)

def press(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

def operation(op):
    global math_op
    math_op = op
    global i
    i = float(e.get().split()[0])
    
    e.insert(END, f" {op} ")

def clr():
    e.delete(0, END)

def eql():
    try:
        data = e.get()
        if math_op in data:
            n2 = float(data.split()[-1]) 
            e.delete(0, END)
            if math_op == '+':
                e.insert(0, i + n2)
            elif math_op == '-':
                e.insert(0, i - n2)
            elif math_op == 'x':
                e.insert(0, i * n2)
            elif math_op == '/':
                e.insert(0, i / n2)
            elif math_op == '%':
                e.insert(0, i * (n2 / 100))
    except:
        e.insert(0, "Error")

def sqt():
    try:
        num = float(e.get())  
        e.delete(0, END)
        e.insert(0, math.sqrt(num)) 
    except:
        e.insert(0, "Error")  


b1 = Button(win, text='1', width=10, bg='grey', fg='white', command=lambda: press(1),relief=RAISED,bd=3)
b1.place(x=10, y=100)

b2 = Button(win, text='2', width=10, bg='grey', fg='white', command=lambda: press(2),relief=RAISED,bd=3)
b2.place(x=100, y=100)

b3 = Button(win, text='3', width=10, bg='grey', fg='white', command=lambda: press(3),relief=RAISED,bd=3)
b3.place(x=190, y=100)

b4 = Button(win, text='4', width=10, bg='grey', fg='white', command=lambda: press(4),relief=RAISED,bd=3)
b4.place(x=10, y=150)

b5 = Button(win, text='5', width=10, bg='grey', fg='white', command=lambda: press(5),relief=RAISED,bd=3)
b5.place(x=100, y=150)

b6 = Button(win, text='6', width=10, bg='grey', fg='white', command=lambda: press(6),relief=RAISED,bd=3)
b6.place(x=190, y=150)

b7 = Button(win, text='7', width=10, bg='grey', fg='white', command=lambda: press(7),relief=RAISED,bd=3)
b7.place(x=10, y=200)

b8 = Button(win, text='8', width=10, bg='grey', fg='white', command=lambda: press(8),relief=RAISED,bd=3)
b8.place(x=100, y=200)

b9 = Button(win, text='9', width=10, bg='grey', fg='white', command=lambda: press(9),relief=RAISED,bd=3)
b9.place(x=190, y=200)

b10 = Button(win, text='0', width=10, bg='grey', fg='white', command=lambda: press(0),relief=RAISED,bd=3)
b10.place(x=10, y=250)


b11 = Button(win, text='/', width=8, bg='black', fg='white', command=lambda: operation('/'),relief=RAISED,bd=3)
b11.place(x=280, y=100)

b12 = Button(win, text='x', width=8, bg='black', fg='white', command=lambda: operation('x'),relief=RAISED,bd=3)
b12.place(x=280, y=150)

b13 = Button(win, text='-', width=8, bg='black', fg='white', command=lambda: operation('-'),relief=RAISED,bd=3)
b13.place(x=190, y=250)

b14 = Button(win, text='%', width=8, bg='black', fg='white', command=lambda: operation('%'),relief=RAISED,bd=3)
b14.place(x=100, y=250)

b15 = Button(win, text='+', width=8, height=5, bg='black', fg='white', command=lambda: operation('+'),relief=RAISED,bd=3)
b15.place(x=280, y=200)

b16 = Button(win, text='.', width=8, bg='black', fg='white', command=lambda: press('.'),relief=RAISED,bd=3)
b16.place(x=10, y=300)


b17 = Button(win, text='C', width=8, bg='darkred', fg='white', command=clr,relief=RAISED,bd=3)
b17.place(x=190, y=300)

b18 = Button(win, text='=', width=8, bg='black', fg='white', command=eql,relief=RAISED,bd=3)
b18.place(x=280, y=300)

b19 = Button(win, text='√', width=8, bg='black', fg='white', command=sqt,relief=RAISED,bd=3)
b19.place(x=100, y=300)

win.mainloop()
