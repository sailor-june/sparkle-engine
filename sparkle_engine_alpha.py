import tkinter
import random
import math
from tkinter import *
from tkinter import ttk

##defining the grid
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
frm.columnconfigure(0, weight=0)
frm.columnconfigure(1, weight=0)
frm.columnconfigure(2, weight=1)
frm.rowconfigure(0, weight=1)
frm.rowconfigure(1,weight=0)
frm.rowconfigure(2,weight=0)
root.geometry(newGeometry="280x170")


##power level guts go here
powerlevel=StringVar()
power = 100

powerlevel.set(str(power))
def plus():
    power = int(powerlevel.get())
    power +=1
    powerlevel.set(str(power))
def minus():
    power = int(powerlevel.get())
    power -=1
    powerlevel.set(str(power))

##sparkle engine goes here

sparkles = ["`","*","-",".","'",'"',",","@"]
magout = StringVar()
magout.set('.')

def magic():
    ingredients=[]
    mana=magout.get()
    spell =random.choice(sparkles)
    ingredients.append(mana)
    ingredients.append(spell)

    if len(ingredients[0])>8:
        drain=[]
        for i in ingredients[0]:
            drain.append(i)
        drain.remove(drain[0])
        ingredients[0]=''.join(drain)
    cast = ''.join(ingredients)
    print(cast)
    print('**********')
    print(ingredients[0])
    print(len(ingredients[0]))
    magout.set(cast)

##widgets to populate the grid
box = tkinter.Message(frm, textvariable=magout)
label_0 = Label(frm, text = "power level:")
label_1 = Label(frm, textvariable=powerlevel)

##positioning widgets

box.grid(column=0, row=0, columnspan=3)
label_0.grid(column=1,row=1)
label_1.grid(column=1,row=2)


#buttons go here
ttk.Button(frm, text="+", command=plus).grid(column=0, row=3)
ttk.Button(frm, text="-", command=minus).grid(column=2, row=3)
ttk.Button(frm, text="sparkle", command=magic).grid(column=1,row=4)

## a slider, because why not?
w = Scale(frm, from_=0, to=200, orient=HORIZONTAL).grid(column=1, row=5)
root.mainloop()
