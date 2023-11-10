#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from datetime import datetime

def update_time():
    current_time = datetime.now().time()
    var_time.set(f"{current_time.hour}:{current_time.minute}:{current_time.second}")
    Calculator.after(1000, update_time)
    
def Del():
    n=len(text_Var.get())
    display.delete(n-1)
    
def Clear():
    display.delete(0,END)

def click(number):
    display.config(fg="black")
    n=len(text_Var.get())
    display.insert(n,number)
    
def Equal():
    op=list()
    data=list()
    equation=text_Var.get()
    
    for i in equation :
        if i not in "0123456789":
            op.append(i)
            
    if len(op)==1:
        data=equation.split(op[0])
        data=[int(i) for i in data]
        
        if op[0]=='+':
            Sum(data)
            
        elif op[0]=='-':
            Sub(data)
            
        elif op[0]=='/':
            Dev(data)
            
        elif (op[0]=='x') or (op[0]=='*'):
            Mult(data)
            
        else:
            display.config(fg="red")
            text_Var.set('Error...')
    
    else:
        display.config(fg="red")
        text_Var.set('Error...')
    
def Sum(l):
    s=0
    for i in l:
        s+=int(i)
    display.delete(0,END)
    text_Var.set(s)
    
def Sub(l):
    s=l[0]
    for i in l[1:]:
        s-=int(i)
    display.delete(0,END)
    text_Var.set(s)
    
def Dev(l):
    d=l[0]
    for i in l[1:]:
        d/=int(i)
    display.delete(0,END)
    text_Var.set(d)
    
def Mult(l):
    m=1
    for i in l:
        m*=int(i)
    display.delete(0,END)
    text_Var.set(m)

Calculator = Tk()
Calculator.title("MyCalculator")
Calculator.iconbitmap('Calculator.ico')

text_Var=StringVar()
display=Entry(Calculator,font=('arial', 11, 'bold'), textvariable=text_Var, bd=7)

var_time = StringVar()
time_label = Label(Calculator, textvariable=var_time, font=("arial",10), padx=22, pady=9, bg="#F3E99F")

btnDel=Button(Calculator, text="Del", command=Del, font=("arial",13, "bold"), padx=6, pady=5, bg="#17A589")
btnClear=Button(Calculator, text="C", command=Clear, font=("arial",15, "bold"), padx=8, pady=0.9, bg="red")

btn9=Button(Calculator, text="9", command=lambda : click(9), font=("arial",15, "bold"), padx=10, pady=5)
btn8=Button(Calculator, text="8", command=lambda : click(8), font=("arial",15, "bold"), padx=10, pady=5)
btn7=Button(Calculator, text="7", command=lambda : click(7), font=("arial",15, "bold"), padx=10, pady=5)
btn6=Button(Calculator, text="6", command=lambda : click(6), font=("arial",15, "bold"), padx=10, pady=5)
btn5=Button(Calculator, text="5", command=lambda : click(5), font=("arial",15, "bold"), padx=10, pady=5)
btn4=Button(Calculator, text="4", command=lambda : click(4), font=("arial",15, "bold"), padx=10, pady=5)
btn3=Button(Calculator, text="3", command=lambda : click(3), font=("arial",15, "bold"), padx=10, pady=5)
btn2=Button(Calculator, text="2", command=lambda : click(2), font=("arial",15, "bold"), padx=10, pady=5)
btn1=Button(Calculator, text="1", command=lambda : click(1), font=("arial",15, "bold"), padx=10, pady=5)
btn0=Button(Calculator, text="0", command=lambda : click(0), font=("arial",15, "bold"), padx=10, pady=5)

btnSum=Button(Calculator, text="+", command=lambda : click('+'), font=("arial",15, "bold"), padx=10, pady=5, bg="#03ed27")
btnSub=Button(Calculator, text="-", command=lambda : click('-'), font=("arial",15, "bold"), padx=12, pady=5, bg="#a15dea")
btnDevide=Button(Calculator, text="/", command=lambda : click('/'), font=("arial",15, "bold"), padx=12, pady=5, bg="#94e5df")
btnMultip=Button(Calculator, text="x", command=lambda : click('x'), font=("arial",15, "bold"), padx=10, pady=5, bg="#ff6f69")

btnEqual=Button(Calculator, text="=", command=Equal, font=("arial",15, "bold"), padx=35.5, pady=5, bg="#3498DB")


display.grid(row=0, column=0, columnspan=4)

time_label.grid(row=2, column=0, columnspan=2)
btnClear.grid(row=2, column=2)
btnDel.grid(row=2, column=3)

btnSum.grid(row=3, column=3)
btnSub.grid(row=4, column=3)
btnDevide.grid(row=5, column=3)
btnMultip.grid(row=6, column=3)

btn9.grid(row=3, column=2)
btn8.grid(row=3, column=1)
btn7.grid(row=3, column=0)

btn6.grid(row=4, column=2)
btn5.grid(row=4, column=1)
btn4.grid(row=4, column=0)

btn3.grid(row=5, column=2)
btn2.grid(row=5, column=1)
btn1.grid(row=5, column=0)

btn0.grid(row=6, column=2)

btnEqual.grid(row=6, column=0, columnspan=2)

update_time()

Calculator.mainloop()

