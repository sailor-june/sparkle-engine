# import time
import tkinter
import random
import math
from tkinter import *
from tkinter import ttk

# defining the grid
root = Tk()
root.title("SPARKLE ENGINE ALPHA V1.1")
frm = ttk.Frame(root, padding=10)
outfrm = ttk.Frame(root, padding=5)

frm.grid(row=1, column=1)
outfrm.grid(row=0, column=1, columnspan=3)

outfrm.columnconfigure(1, weight=1)
frm.columnconfigure(0)
frm.columnconfigure(1)
frm.columnconfigure(2)
frm.rowconfigure(0)
frm.rowconfigure(1)
frm.rowconfigure(2)
root.geometry(newGeometry="280x180")

sparkles = ["`", "*", "-", ".", "'", '"', ",", "@", "~"]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Global variables. I will never apologize.
powerlevel = DoubleVar()
powerlevel.set(100)
magout = StringVar()
color = StringVar()
magout.set('.')
color.set('black')


# power level guts go here
def plus():
    power = int(powerlevel.get())
    power += 1
    powerlevel.set(power)


def minus():
    power = int(powerlevel.get())
    power -= 1
    powerlevel.set(power)


# sparkle generator goes here
def magic():
    ingredients = []
    mana = magout.get()
    spell = random.choice(sparkles)
    ingredients.append(mana)
    ingredients.append(spell)
    if len(ingredients[0]) > 8:
        drain = []
        for i in ingredients[0]:
            drain.append(i)
        drain.remove(drain[0])
        ingredients[0] = ''.join(drain)
    cast = ''.join(ingredients)
    if r1_v.get():
        color.set(random.choice(colors))
        box["fg"] = color.get()
    else:
        color.set('black')
        vibe.set(vibe.get() + random.randint(-70, 70))

    magout.set(cast)
    """"
    this is for debugging magic()
    print(cast)
    print('**********')
    print(ingredients[0])
    print(len(ingredients[0]))
    print(color.get())
    """


vibe = tkinter.IntVar()

# the vibe meter
w = Scale(frm, from_=1, to=200, orient=HORIZONTAL, variable=vibe)
w.grid(column=1, row=5)


def harmony():
    alpha = math.floor(powerlevel.get())
    beta = math.floor(vibe.get())
    box["fg"]='black'
    print(alpha, beta)
    if alpha > beta:
        index = range(beta, alpha)
    elif alpha < beta:
        index = range(alpha, beta)
    elif alpha == beta:
        harmonic = 100
        index = [100]
        powerlevel.set(harmonic)
        vibe.set(harmonic)
    n = len(index)
    if n % 2 == 0:
        median1 = index[n // 2]
        median2 = index[n // 2 - 1]
        harmonic = (median1 + median2) // 2

    else:
        harmonic = math.floor(index[(n // 2)])

    if harmonic > 200:
        harmonic = 200
    print(harmonic)
    print(r1_v.get())

    powerlevel.set(harmonic)
    vibe.set(harmonic)


# widgets to populate the grid
box = tkinter.Message(outfrm, textvariable=magout, width=93, fg=color.get())

label_0 = Label(frm, text="power level:")
label_1 = Label(frm, textvariable=powerlevel)

# positioning widgets

box.grid(column=0, row=0, columnspan=3)
label_0.grid(column=1, row=1)
label_1.grid(column=1, row=2)

# buttons go here
ttk.Button(frm, text="+", command=plus).grid(column=0, row=3)
ttk.Button(frm, text="-", command=minus).grid(column=2, row=3)
ttk.Button(frm, text="HARMONIZE", command=harmony).grid(column=1, row=3)
ttk.Button(frm, text="CAST", command=magic).grid(column=1, row=4)

r1_v = tkinter.BooleanVar()

r1 = ttk.Radiobutton(frm, variable=r1_v, value=0)
r2 = ttk.Radiobutton(frm, variable=r1_v, value=1)
r1.grid(row=4, column=0)
r2.grid(row=4, column=2)
root.mainloop()
