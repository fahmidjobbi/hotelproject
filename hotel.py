from re import T
import tkinter as tk
from PIL import Image,ImageTk
from email.message import Message
from timeit import repeat
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import Tk, Frame, Menu, ttk,Toplevel
from PIL import Image,ImageTk
import os
import tkinter.filedialog as filedialog
import numpy as np
import joblib as joblib
import pandas as pd 
from keras.models import load_model
from tkinter.ttk import *
#kkkkkk
#hotel projet

#create the main window

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

print('hello')
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.filename = None

        self.title("Hotel Review")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        vo= str(os.path.abspath(os.getcwd()))+r'\hotel.ico'
        self.iconbitmap(vo)
       
        

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
    
        # ============ frame_right ============
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text ='Predict Review', 
                                                command=self.classify)
                                               
        self.button_1.grid(row=1, column=0, pady=10, padx=20)

        
        
        
        self.entry = tk.Text(master=self.frame_right,
                                            width=40,
                                            height=10,
                                            fg=("gray38"),
                                            bg=("white"),
                                            font=("Arial", 12),
                                            borderwidth=1,
                                            relief=tkinter.SOLID
                                            ) 
        
        self.entry.grid(row=8, column=0, columnspan=2, pady=40, padx=40, sticky="nsew")
        
        
        
    def on_closing(self,event=0):
    #delete tmp files if exist  
    #delete tmp files if exist
       
   
        # directory
        dir = str(os.path.abspath(os.getcwd()))+r'\tmp'
   
        # path
        try:
            for file in os.scandir(dir):
                os.remove(file.path)
       
        except:
            pass
       
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            
    
    

            
          
            
     
    
    def result(self):
        classifer = self.classify(self.filename)

        
        self.label = customtkinter.CTkLabel(master=self.frame_right, text=classifer, foreground='green',width=350, 
                                            height=380,bg_color='white',corner_radius=10,text_color='green',
                                            anchor='center',text_font=('Arial', 30, 'bold'))
                                            
     
                                           
      
        self.label.grid(row=4, column=1, pady=10, padx=20)
        
        

  
    def classify(self):
        
        model=joblib.load('modelhotel.sav')
        #dictionary to label all traffic signs class.
        classes = { 
        'happy':'Good news it was  a happy experience',
        'not happy':'Sorry it was not a happy experience',
 
        }
        
        pred = model.predict([self.entry.get("1.0","end-1c")])
        sign=classes[pred[0]]
        
        print(sign)
       
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=sign,
                                                   height=100,
                                                   fg_color=("white", "gray38"),
                                                   text_color=("green", "gray38"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=5, pady=5)
        
 
       
        


# ============ main ============
            

class Example(Frame):
    
        def __init__(self):
            super().__init__()

            self.initUI()


        def initUI(self):

            self.master.title("Hotel Review")

            menubar = Menu(self.master)
            self.master.config(menu=menubar)

            fileMenu = Menu(menubar)
            fileMenu.add_command(label="Exit", command=self.onExit)
            menubar.add_cascade(label="File", menu=fileMenu)
            
            editMenu = Menu(menubar)
            editMenu.add_command(label="Undo")
            editMenu.add_separator()
            editMenu.add_command(label="Cut")
            editMenu.add_command(label="Copy")
            editMenu.add_command(label="Paste")
            editMenu.add_separator()
            editMenu.add_command(label="Select All")
            menubar.add_cascade(label="Edit", menu=editMenu)
          
            
            helpMenu = Menu(menubar)
            helpMenu.add_command(label="About", command=self.onAbout)
            menubar.add_cascade(label="Help", menu=helpMenu)
            
            
          
            
            
            #set HTML content
            
            #print(frame.html.cget("zoom"))           

            #frame.load_website("https://app.powerbi.com/reportEmbed?reportId=e7a66a17-9821-4656-966b-b6e21a4b8ed6&autoAuth=true&ctid=889cdbee-d881-42dc-bd06-ad3237c34a53&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXNvdXRoLWFmcmljYS1ub3J0aC1hLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D") #load a website
        
            #frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
            
            

            
           
        
            


        def onExit(self):

            self.quit()   
            
        

        
        ## FUNCTION TO SHOW ABOUT DIALOG     
        def onAbout(self):
            new_window=Toplevel(self.master)
            new_window.geometry("800x400+50+50")
            new_window.attributes('-alpha', 1)
            new_window.title("About")
            new_window.resizable(False,False)
            lbl=customtkinter.CTkLabel(master=new_window,
                                                   text=
                                                   '''Auteur : FAHMI DJOBBI \n \n \t'''+
                                                    '''Version : 1.0 \n \n \t''',


                                                   
                                                   height=150,
                                                   fg_color=("yellow"),  #<- custom tuple-color
                                                   justify="left",
                                                   )

            lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="we")
            lbl.configure(font=("Arial", 9, "bold"))

             
 
 
 
 
 
 
 ######################### END  APP ###################################               

if __name__ == "__main__":
    app = App()
    app1=Example()
    app.mainloop()