import tkinter as tk
import math

root=tk.Tk()
root.geometry("450x265")
root.resizable(0,0)

e1=tk.Entry(root,bg="#BBB",bd=5,width=71,highlightbackground="#304179",highlightthickness=7)
e1.grid(columnspan=5)

first=0
second=0
symbol=''

def on_click(n):
    e1.insert(tk.END,n)

def all_clear():
    e1.delete(0,tk.END)

def delete():
    e1.delete(len(e1.get())-1)

def dot():
    e1.insert(len(e1.get()),'.')

def abs():
    n=e1.get()
    if float(n)<0:
        e1.delete(0,tk.END)
        e1.insert(0,str(float(n)*-1))
    else:
        e1.delete(0,tk.END)
        e1.insert(0,n)

def add():
    global first
    global symbol
    symbol='+'
    first=e1.get()
    e1.delete(0, tk.END)

def sub():
    global first
    global symbol
    symbol='-'
    first=e1.get()
    e1.delete(0,tk.END)
    e1.insert(0,'-')

def mul():
    global first
    global symbol
    symbol='*'
    first=e1.get()
    e1.delete(0,tk.END)

def div():
    global first
    global symbol
    symbol='/'
    first=e1.get()
    e1.delete(0,tk.END)

def mod():
    global first
    global symbol
    first=e1.get()
    symbol='mod'
    e1.delete(0,tk.END)

def div():
    global first
    global symbol
    first=e1.get()
    symbol='div'
    e1.delete(0,tk.END)

def fact():
    global first
    s=1
    first=int(e1.get())
    e1.delete(0,tk.END)
    for i in range(1,first):
        s=i*s
    e1.insert(0,s*first)

def e():
    e1.delete(0,tk.END)
    e1.insert(0,'2.71828')

def sin():
    a=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,math.sin(math.radians(a)))

def cos():
    a=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,math.cos(math.radians(a)))

def tan():
    a=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,math.tan(math.radians(a)))

def cot():
    a=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,1/(math.tan(math.radians(a))))

def pi():
    e1.delete(0,tk.END)
    e1.insert(0,22/7)

def x2():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,first*first)

def x3():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,first*first*first)

def xn():
    global first
    global symbol
    symbol='xn'
    first=float(e1.get())
    e1.delete(0,tk.END)

def invx():
    first=e1.get()
    e1.delete(0,tk.END)
    e1.insert(0,first*first)

def x10():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,pow(10,first))

def root2():
    first=float(e1.get())
    e1.insert(0,math.sqrt(first))

def root3():
    first=float(e1.get())
    e1.insert(0,math.cbrt(first))

def rootn():
    global first
    global symbol
    symbol='rootn'
    first=float(e1.get())
    e1.delete(0,tk.END)

def log10():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,math.log(first,10))

def ln():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,math.log(first))

def invx():
    first=float(e1.get())
    e1.delete(0,tk.END)
    e1.insert(0,1/first)

def rem():
    global first
    global symbol
    first=float(e1.get())
    symbol='%'
    e1.delete(0,tk.END)

def equal():
    global second
    second=e1.get()
    e1.delete(0,tk.END)

    if symbol=='+':
        e1.insert(0,float(first)+float(second))
    elif symbol=='-':
        e1.insert(0,float(first)-float(second))
    elif symbol=='*':
        e1.insert(0,float(first)*float(second))
    elif symbol=='/':
        e1.insert(0,float(first)/float(second))
    elif symbol=='mod' or symbol=='%':
        e1.insert(0,float(first)%float(second))
    elif symbol=='div':
        e1.insert(0,float(first)//float(second))
    elif symbol=='xn':
        s=1
        for i in range (1,int(second)):
            s=s*first
        e1.insert(0,s)
    elif symbol=='rootn':
        e1.insert(0,first**(1/float(second)))

#ROW 1
b_abs=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="abs",command=abs)
b_abs.grid(row=1,column=0)
b_mod=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="mod",command=mod)
b_mod.grid(row=1,column=1)
b_div=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="div",command=div)
b_div.grid(row=1,column=2)
b_x=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="x!",command=fact)
b_x.grid(row=1,column=3)
b_e=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="e",command=e)
b_e.grid(row=1,column=4)

#ROW 2
b_sin=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="sin",command=sin)
b_sin.grid(row=2,column=0)
b_cos=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="cos",command=cos)
b_cos.grid(row=2,column=1)
b_tan=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="tan",command=tan)
b_tan.grid(row=2,column=2)
b_cot=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="cot",command=cot)
b_cot.grid(row=2,column=3)
b_pi=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="π",command=pi)
b_pi.grid(row=2,column=4)

#ROW 4

b_x2=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="x²",command=x2)
b_x2.grid(row=3,column=0)
b_x3=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="x³",command=x3)
b_x3.grid(row=3,column=1)
b_xn=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="xⁿ",command=xn)
b_xn.grid(row=3,column=2)
b_invx=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="x⁻¹",command=invx)
b_invx.grid(row=3,column=3)
b_10x=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="10ˣ",command=x10)
b_10x.grid(row=3,column=4)

#ROW 5

b_root2=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="²√",command=root2)
b_root2.grid(row=4,column=0)
b_root3=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="³√",command=root3)
b_root3.grid(row=4,column=1)
b_root=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="√",command=rootn)
b_root.grid(row=4,column=2)
b_log10=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="log₁₀",command=log10)
b_log10.grid(row=4,column=3)
b_ln=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark grey",fg="white",relief="raised",text="ln",command=ln)
b_ln.grid(row=4,column=4)

#ROW 6

b_7=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="7",command=lambda:on_click(7))
b_7.grid(row=5,column=0)
b_8=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="8",command=lambda:on_click(8))
b_8.grid(row=5,column=1)
b_9=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="9",command=lambda:on_click(9))
b_9.grid(row=5,column=2)
b_del=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark orange",fg="white",relief="raised",text="DEL",command=delete)
b_del.grid(row=5,column=3)
b_ac=tk.Button(root,font="sansserif 10 bold",width=10,bg="dark orange",fg="white",relief="raised",text="AC",command=all_clear)
b_ac.grid(row=5,column=4)

#ROW 7

b_4=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="4",command=lambda:on_click(4))
b_4.grid(row=6,column=0)
b_5=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="5",command=lambda:on_click(5))
b_5.grid(row=6,column=1)
b_6=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="6",command=lambda:on_click(6))
b_6.grid(row=6,column=2)
b_mul=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="*",command=mul)
b_mul.grid(row=6,column=3)
b_div=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="/",command=div)
b_div.grid(row=6,column=4)

#ROW 8

b_1=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="1",command=lambda:on_click(1))
b_1.grid(row=7,column=0)
b_2=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="2",command=lambda:on_click(2))
b_2.grid(row=7,column=1)
b_3=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="3",command=lambda:on_click(3))
b_3.grid(row=7,column=2)
b_add=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="+",command=add)
b_add.grid(row=7,column=3)
b_sub=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="-",command=sub)
b_sub.grid(row=7,column=4)

#ROW 9

b_0=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="0",command=lambda:on_click(0))
b_0.grid(row=8,column=0)
b_dot=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text=".",command=dot)
b_dot.grid(row=8,column=1)
b_mod=tk.Button(root,font="sansserif 10 bold",width=10,bg="grey",fg="white",relief="raised",text="%",command=rem)
b_mod.grid(row=8,column=2)
b_equal=tk.Button(root,font="sansserif 10 bold",width=21,bg="grey",fg="white",relief="raised",text="=",command=equal)
b_equal.grid(row=8,columnspan=2,column=3)


root.mainloop()