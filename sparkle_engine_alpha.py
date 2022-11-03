# import time
import tkinter
import random
import math
from tkinter import *
from tkinter import ttk

# defining the grid
root = Tk()
root.title("SPARKLE ENGINE ALPHA V1.4")
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
powerlevel = IntVar()
mana=IntVar()
r1_v = BooleanVar()
magout = StringVar()
color = StringVar()
vibe = IntVar()
magout.set('.')
color.set('black')
powerlevel.set(0)
mana.set(5)
# power level guts go here
def plus():
    powerlevel.set(powerlevel.get()+random.randint(1,5))
    vibe.set(vibe.get()-random.randint(1,5))
    if vibe.get()<=100:
        plusBut["state"]=DISABLED
    if powerlevel.get()>0:
        castBut['state']=ACTIVE

def minus():
    powerlevel.set(powerlevel.get()-1)
    vibe.set(vibe.get()+random.randint(-10,25))
    if powerlevel.get()<=0:
        minusBut['state']=DISABLED
        castBut['state']=DISABLED
    if vibe.get()>100:
        plusBut['state']=ACTIVE
    if vibe.get()==200:
        minusBut['state']=DISABLED


# sparkle generator goes here
def magic():
    ingredients = []
    magIn = magout.get()
    spell = random.choice(sparkles)
    ingredients.append(magIn)
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
        powerlevel.set(math.floor(powerlevel.get()-random.randint(1,10)))
    else:
        color.set('black')
        box["fg"] = color.get()
        powerlevel.set(powerlevel.get()-1)
        vibe.set(vibe.get() + random.randint(-70, 70))
    if vibe.get()<100:
        plusBut["state"]=DISABLED
    else:
        plusBut['state']=ACTIVE
    if vibe.get()==200:
        minusBut['state']=DISABLED
    else:
        minusBut['state']=ACTIVE

    if powerlevel.get()<=0:
        castBut["state"]=DISABLED
        minusBut['state']=DISABLED
    else:
        minusBut['state']=ACTIVE

    magout.set(cast)
    """"
    this is for debugging magic()
    print(cast)
    print('**********')
    print(ingredients[0])
    print(len(ingredients[0]))
    print(color.get())
    """







def harmony():
    alpha = math.floor(powerlevel.get())
    beta = math.floor(vibe.get())
    box["fg"]='black'
    print(alpha, beta)
    if alpha == beta:
        powerlevel.set(powerlevel.get()+random.randint(-100,100))
        if powerlevel.get()<0:
            powerlevel.set(0)
        vibe.set(vibe.get()+random.randint(-100,100))
        index = [100]
    else:
        if alpha > beta:
            index = range(beta, alpha)
        elif alpha < beta:
            index = range(alpha, beta)



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

        if powerlevel.get()<=0 and vibe.get()==1:
            powerlevel.set(10)
        else:
            powerlevel.set(harmonic)
            vibe.set(harmonic)
        if powerlevel.get() > 0:
            castBut["state"] = ACTIVE
        if vibe.get()>=100:
            plusBut['state']=ACTIVE
        if vibe.get() == 200:
            minusBut['state'] = DISABLED
        else:
            minusBut['state'] = ACTIVE



# widgets to populate the grid
box = tkinter.Message(outfrm, textvariable=magout, width=93, fg=color.get())

label_0 = Label(frm, text="power level:")
label_1 = Label(frm, textvariable=powerlevel)



# buttons go here
plusBut=ttk.Button(frm, text="+", command=plus)
minusBut=ttk.Button(frm, text="-", command=minus)
harmonyBut=ttk.Button(frm, text="HARMONIZE", command=harmony)
castBut=ttk.Button(frm, text="CAST", command=magic)
vibeMeter = Scale(frm, from_=1, to=200, orient=HORIZONTAL, variable=vibe, state=DISABLED)


r1 = ttk.Radiobutton(frm, variable=r1_v, value=0)
r2 = ttk.Radiobutton(frm, variable=r1_v, value=1)
# positioning widgets

box.grid(column=0, row=0, columnspan=3)
label_0.grid(column=1, row=1)
label_1.grid(column=1, row=2)
plusBut.grid(column=0, row=3)
minusBut.grid(column=2, row=3)
harmonyBut.grid(column=1, row=3)
castBut.grid(column=1, row=4)
vibeMeter.grid(column=1, row=5)
r1.grid(row=4, column=0)
r2.grid(row=4, column=2)



root.mainloop()
