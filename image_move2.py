from tkinter import *
from tkinter import ttk

pencere=Tk()

resim= PhotoImage(file="logo.gif")

canvas=Canvas(pencere, width=500,height=600)
canvas.grid()
yeni=canvas.create_image(270, 300,image=resim)

def saga_kaydir(*args):
	canvas.move(yeni,+5,0)
	canvas.update()
dugmesag = ttk.Button(text="SAĞ", command =saga_kaydir).grid(row=0,column=2, sticky=E)
pencere.bind("<Right>",saga_kaydir)
def sola_kaydir(*args):
	canvas.move(yeni,-5,0 )
	canvas.update()
dugmesol=ttk.Button(text="SOL", command =sola_kaydir).grid(row=0,column=0 ,sticky=W)
pencere.bind("<Left>",sola_kaydir)
def yukari_kaydir(*args):
	canvas.move(yeni, 0, -5)
	canvas.update()
dugme_yukari=ttk.Button(text="YUKARI", command =yukari_kaydir).grid(row=0,column=0 ,sticky=N)
pencere.bind("<Up>",yukari_kaydir)
def asagi_kaydir(*args):
	canvas.move(yeni, 0, +5)
	canvas.update()
dugme_asagi=ttk.Button(text="AŞAĞI", command =asagi_kaydir).grid(row=3,column=0 ,sticky=S)
pencere.bind("<Down>",asagi_kaydir)


mainloop()


