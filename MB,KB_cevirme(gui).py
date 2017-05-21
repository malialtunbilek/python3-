from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        deger = float(mb.get())
        bit.set(1024*deger*1024*8)
    except ValueError:
        pass

root = Tk()
root.title("DEPOLAMA BİRİMİ ÇEVİRME ")

anacerceve = ttk.Frame(root, padding="10 10 12 12")
anacerceve.grid(column=0, row=0, sticky=(N, W, E, S))
anacerceve.columnconfigure(0, weight=1)
anacerceve.rowconfigure(0, weight=1)

liste = ["Byte","KB","MB","GB","TB"]
mb = StringVar()
bit = StringVar()

feet_entry = ttk.Entry(anacerceve, width=7, textvariable=mb)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(anacerceve, textvariable=bit).grid(column=2, row=2, sticky=(W, E))
ttk.Button(anacerceve, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(anacerceve, text="MB").grid(column=3, row=1, sticky=W)
ttk.Label(anacerceve, text="MB ").grid(column=1, row=2, sticky=E)
ttk.Label(anacerceve, text="Bit eder.").grid(column=3, row=2, sticky=W)

for child in anacerceve.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
