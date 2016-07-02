from tkinter import *

def runSimplex():
    global e
    string = e.get()
    print(string)

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
e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Run Simplex',command=runSimplex)
b.pack(side='bottom')
root.mainloop()