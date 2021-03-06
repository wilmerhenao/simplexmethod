from tkinter import *
import numpy as np
import ast as cp
import re

def runSimplex():
    global e
    string = e.get()
    print('objective function entered:', string)
    global TextArea
    dasinput = TextArea.get("0.0",END)
    print('constraints as entered:', dasinput)
    parseobjective(string)

def parseobjective(obje):
    newstr = re.sub('[* ]', '', obje)
    tokenresult = re.split("([+-/*])", newstr)
    # Catch all the expressions that have alphanumeric characters
    vars = []
    for singletoken in tokenresult:
        ischarac = re.search('[a-zA-Z].*$', singletoken)
        if ischarac:
            vars.append(ischarac.group())
    vars = np.unique(vars)
    print(vars)
    print(tokenresult)

root = Tk()

root.title('Name')

# label above the screen that asks for info
Label(root, text="Input the objective function typing variables x1,x2,...:").pack(side=TOP, padx=15, pady=10)

# Radio button to capture the max, min option
var = IntVar()
for text, value in [('Minimize', 1), ('Maximize', 2)]:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(1)

# Entry that gets the input
e = StringVar()
e = Entry(root, width=40)
e.insert(END, 'x + 3y -5*z_1 -7z2 + 8z5 - y + 8spam - eggs')
e.pack()
e.focus_set()

# label above the screen that asks for info
Label(root, text="Type your constraints below:").pack(side=TOP, padx=15, pady=10)

# Entry that gets the constraints
# Entry that gets the input
cs = StringVar()
#text = Text(root, height=10, width=50)
#text.pack()

TextArea = Text()
ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack(expand=YES, fill=BOTH)



b = Button(root,text='Run Simplex',command=runSimplex)
b.pack(side='bottom')
root.mainloop()
