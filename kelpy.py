#Kelpy Editor 1.0.0
#@ 11 / 10/ 2017
#@authour Kelvin Kipkoech 
from tkinter import *
from tkinter import filedialog
import tkinter as tki
import webbrowser


class App(object):

    def __init__(self):
    #Declaring button functions
        def savingFile():
            name  =  filedialog.asksaveasfilename(defaultextension='.py',initialdir = "/",title = "Select file",filetypes = (("python files","*.py"),("all files","*.*")))
            outfile = open(name,"w")
            data = self.txt.get("1.0","end-1c")
            outfile.write(data)
            outfile.close()
        def openingFile():
            self.txt.delete(1.0,END)
            filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("python files","*.py"),("all files","*.*")))
            in_file = open(filename,"r")
            text = in_file.read()
            self.txt.insert(INSERT,text)
            in_file.close()
    
    
        def redoText():
            if len(self.txt.get("1.0", "end-1c")) == 0:
                self.txt.insert(1.0,"The field is empty")
            else:   
               self.txt.edit_separator()
               self.txt.edit_redo()
    
        def undoText():
            if len(self.txt.get("1.0", "end-1c")) == 0:
                self.txt.insert(1.0,"The field is empty")
            else: 
                self.txt.edit_separator()
                self.txt.edit_undo()
            
        def closeKelpy():
             sys.exit()
        def saveasFile():
             name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("python files","*.py"),("all files","*.*")))
             outfile = open(name,"w")
             data = self.txt.get("1.0","end-1c")
             outfile.write(data)
             outfile.close()
        def getHelp():
            webbrowser.open('www.facebook.com/Kelpy-Text-Editor-326790717787089/?ref=bookmarks')
        def clearScreen():
            if len(self.txt.get("1.0", "end-1c")) == 0:
                self.txt.insert(1.0,"The field is empty")
            else:
                self.txt.delete(1.0,END)
            
            
            
      #main class      
        self.root = tki.Tk()
        self.root.title("Kelpy Text Editor 1.0.0")
        self.root.minsize(500,300)
        
     # create a Frame for the Headers
        button_frm = tki.Frame(self.root,width=100,bg="#6B6B96")
        button_frm.pack(fill="both", expand=True)
     #Create buttons
        self.undo = Button(button_frm,command=undoText,text="UNDO",fg="green",font="consolas",relief=RIDGE)
        self.undo.pack(side=LEFT)

        self.redo = Button(button_frm,command=redoText,text="REDO",fg="green",font="consolas",relief=RIDGE)
        self.redo.pack(side=LEFT)

        self.clear = Button(button_frm,command=clearScreen,text="CLEAR",fg="green",font="consolas",relief=RIDGE)
        self.clear.pack(side=LEFT)

        self.save = Button(button_frm,command=savingFile,text="SAVE",fg="green",font="consolas",relief=RIDGE)
        self.save.pack(side=LEFT)

        self.saveas = Button(button_frm,command=saveasFile,text="SAVEAS",fg="green",font="consolas",relief=RIDGE)
        self.saveas.pack(side=LEFT)

        self.open = Button(button_frm,command=openingFile,text="OPEN",fg="green",font="consolas",relief=RIDGE)
        self.open.pack(side=LEFT)

        #self.setting = Button(button_frm,text="SETTING",fg="green",font="consolas",relief=RIDGE)
        #self.setting.pack(side=LEFT)

        self.help = Button(button_frm,command=getHelp,text="HELP",fg="green",font="consolas",relief=RIDGE)
        self.help.pack(side=LEFT)

        self.close = Button(button_frm,command=closeKelpy,text="CLOSE",fg="green",font="consolas",relief=RIDGE)
        self.close.pack(side=LEFT)
        
     
    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)
    

    # create a Text widget 
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("monospace", 11),bg="#DBDBDB",fg="#2A2A55", undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    
app = App()
app.root.mainloop()
