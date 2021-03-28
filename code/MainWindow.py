import tkinter as tk

class BancPuissance(tk.Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.pack()
        self.create_widgets(window)

    def create_widgets(self, window):
        
        # on change la taille de la fenetre pour qu'elle prenne tout l'écran
        screenHeight = self.winfo_screenheight() - 70
        screenWidth = self.winfo_screenwidth()
        window.geometry(str(screenWidth) + "x" + str(screenHeight))
        # on empeche le changement de taille de la fenetre
        window.resizable(width=False, height=False)

    def say_hi(self):
        print("hi there, everyone!")