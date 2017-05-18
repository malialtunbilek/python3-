# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
pencere=Tk()

resim = PhotoImage(file="resim.png")
resim2= PhotoImage(file="logo.gif")

#canvas=Canvas(pencere, width=500,height=600)
#canvas.grid()
#yeni=canvas.create_image(image=resim2)

pencere.geometry("1000x1000+100+100")
orta_satir=5
orta_sutun=5

for satir in range(2,9):
	for sutun in range(2,9):	
		kutu= Label(image=resim ).grid(row=satir ,column=sutun)
bolum= Label(image=resim2).grid(row=orta_satir ,column=orta_sutun)

def saga_kaydir(*args):
	global orta_satir,orta_sutun
	bolum=Label(image=resim).grid(row=orta_satir,column=orta_sutun)
	orta_sutun=orta_sutun+1
	bolum=Label(image=resim2).grid(row=orta_satir,column=orta_sutun)

def sola_kaydir(*args):
	global orta_satir,orta_sutun
	
	bolum=Label(image=resim).grid(row=orta_satir,column=orta_sutun)
	orta_sutun=orta_sutun-1
	bolum=Label(image=resim2).grid(row=orta_satir,column=orta_sutun)
	
	#canvas.move(yeni , -10 , 0)
	#canvas.update()
def yukari(*args):
	global orta_satir,orta_sutun
	bolum=Label(image=resim).grid(row=orta_satir,column=orta_sutun)
	orta_satir=orta_satir-1
	bolum=Label(image=resim2).grid(row=orta_satir,column=orta_sutun)

def asagi(*args):
	global orta_satir,orta_sutun
	bolum=Label(image=resim).grid(row=orta_satir,column=orta_sutun)
	orta_satir=orta_satir+1
	bolum=Label(image=resim2).grid(row=orta_satir,column=orta_sutun)


dugmeust = Button(text="ÜST", command =yukari)
dugmeust.grid(row=0,column=5)

dugmesol = Button(text="SOL", command =sola_kaydir)
dugmesol.grid(row=5,column=0)


dugmesag = Button(text="SAĞ", command =saga_kaydir)
dugmesag.grid(row=5,column=50)

dugmealt = Button(text="ALT",command = asagi)
dugmealt.grid(row=20,column=5)

pencere.bind("<Down>",asagi)																											
pencere.bind("<Left>",sola_kaydir)
pencere.bind("<Right>",saga_kaydir)
pencere.bind("<Up>",yukari)

mainloop()