from tkinter import *

def runSimplex():
    global e
    string = e.get()
    print(string)

root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Run Simplex',command=runSimplex)
b.pack(side='bottom')
root.mainloop()