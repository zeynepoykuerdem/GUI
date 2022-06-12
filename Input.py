from tkinter import *


class Input:
    global numberOfIteration
    global chosenColors

    def __init__(self):
        self.taking_input()

    def taking_input(self):
        def update_label():
            output_label['text'] = ent1.get()
            with open("text.txt", "w") as f:
                f.write(ent1.get())
                f.close()

        def start():
            self.numberOfIteration = spinbox.get()
            win.destroy()

        # Initialize window
        win = Tk()
        win.geometry('1000x400')
        win.title('MapColoring')
        # Initialize input frame
        input_frame = Frame(win)
        input_frame.pack(anchor=NE)
        input_frame.grid(column=0, padx=10, pady=10)
        # Initialize input label
        label1 = Label(input_frame, text='Enter graph')
        label1.grid(row=0)
        # Initialize input entry
        ent1 = Entry(input_frame)
        ent1.grid(row=1, padx=10)
        # Initialize output label
        output_label = Label(win, text='')
        output_label.grid(column=2, row=0, padx=100)
        # Initialize input button
        button1 = Button(input_frame, text='View graph', command=update_label)
        button1.grid(row=3, pady=10)
        button2 = Button(input_frame, text='Confirm', command=start)
        button2.grid(row=4, pady=10)
        label2 = Label(input_frame, text='Choose iteration')
        label2.grid(column=1, row=0)
        spinbox = Spinbox(input_frame, from_=0, to=50)
        spinbox.grid(column=1, row=1, pady=10)

        win.mainloop()

        win2 = Tk()  # creating the main window and storing the window object in 'win'
        win2.title('Menu')  # setting title of the window
        top = Frame(win2, bg='white', height=500, width=500)
        top.pack()

        def start2():
            win2.destroy()

        def check():
            txt.delete(1.0, END)
            string = ''

            if (cb_var1.get()):
                string = string + 'Red\t'

            if (cb_var2.get()):
                string = string + 'Blue\t'

            if (cb_var3.get()):
                string = string + 'Green\t'

            if (cb_var4.get()):
                string = string + 'Pink\t'

            if (cb_var5.get()):
                string = string + 'Black\t'

            if (cb_var6.get()):
                string = string + 'Yellow\t'

            if (cb_var7.get()):
                string = string + 'Orange\t'

            if (cb_var8.get()):
                string = string + 'White\t'

            if (cb_var9.get()):
                string = string + 'Purple\t'

            if (cb_var10.get()):
                string = string + 'Brown\t'

            string = list(string.split())
            self.chosenColors = list(string)
            self.chosenColors = set(self.chosenColors)
            txt.insert(1.0, string)

        cb_var1 = IntVar()

        cb1 = Checkbutton(top, text='Red', bg='red', variable=cb_var1, onvalue=1, offvalue=0, height=3, width=20)
        cb_var2 = IntVar()
        cb2 = Checkbutton(top, text='Blue', bg='blue', variable=cb_var2, onvalue=1, offvalue=0, height=3, width=20)
        cb_var3 = IntVar()
        cb3 = Checkbutton(top, text='Green', bg='green', variable=cb_var3, onvalue=1, offvalue=0, height=3, width=20)
        cb_var4 = IntVar()
        cb4 = Checkbutton(top, text='Pink', bg='pink', variable=cb_var4, onvalue=1, offvalue=0, height=3, width=20)
        cb_var5 = IntVar()
        cb5 = Checkbutton(top, text='Black', bg='black', fg='orange', variable=cb_var5, onvalue=1, offvalue=0, height=3,
                          width=20)
        cb_var6 = IntVar()
        cb6 = Checkbutton(top, text='Yellow', bg='yellow', variable=cb_var6, onvalue=1, offvalue=0, height=3, width=20)
        cb_var7 = IntVar()
        cb7 = Checkbutton(top, text='Orange', bg='orange', variable=cb_var7, onvalue=1, offvalue=0, height=3, width=20)
        cb_var8 = IntVar()
        cb8 = Checkbutton(top, text='White', bg='white', variable=cb_var8, onvalue=1, offvalue=0, height=3, width=20)
        cb_var9 = IntVar()
        cb9 = Checkbutton(top, text='Purple', bg='purple', variable=cb_var9, onvalue=1, offvalue=0, height=3, width=20)
        cb_var10 = IntVar()
        cb10 = Checkbutton(top, text='Brown', bg='brown', variable=cb_var10, onvalue=1, offvalue=0, height=3, width=20)
        txt = Text(top, height=2, width=50)

        btn = Button(top, text="Done", command=check)

        btn2 = Button(top, text="Exit", command=start2)

        cb1.pack()
        cb2.pack()
        cb3.pack()
        cb4.pack()
        cb5.pack()
        cb6.pack()
        cb7.pack()
        cb8.pack()
        cb9.pack()
        cb10.pack()

        txt.pack()
        btn.pack(side=RIGHT)
        btn2.pack(side=RIGHT)

        win2.mainloop()
