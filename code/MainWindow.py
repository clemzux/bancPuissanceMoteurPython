import tkinter as tk

class BancPuissance(tk.Frame):

    def __init__(self, window=None):

        super().__init__(window)
        self.window = window
        #self.pack()
        self.configureWindow(window)
        self.createWidgets(window)
    
    def createWidgets(self, window):
        
        self.createMenuBar(window)
        self.createButtons()
        self.createRecordList()

    def createRecordList():

        
    
    def createButtons(self):
        
        # bouton pour ouvrir un fichier audio
        openButton = tk.Button(text="Ouvrir", width=11)
        openButton.grid(row=0, column=0, ipadx=5, pady=5)

        photoButton = tk.Button(text="Photo", width=11)
        photoButton.grid(row=0, column=1, ipadx=5, pady=5)

        overLaysButton = tk.Button(text="Overlays", width=11)
        overLaysButton.grid(row=0, column=2, ipadx=5, pady=5)

        optionButton = tk.Button(text="Options", width=11)
        optionButton.grid(row=0, column=3, ipadx=5, pady=5)

        startRecButton = tk.Button(text="Commencer enregistrement", width=24)
        startRecButton.grid(row=0, column=4, ipadx=5, pady=5)

        stopRecButton = tk.Button(text="Stopper enregistrement", width=24)
        stopRecButton.grid(row=0, column=5, ipadx=5, pady=5)

    def createMenuBar(self, window):

        menuBar = tk.Menu(self)

        # fichier
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuFile.add_command(label="Exit", command=self.quit)
        menuBar.add_cascade( label="Fichier", menu=menuFile)

        # editer
        menuEdit = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade( label="Edit", menu=menuEdit)

        # help
        menuHelp = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade( label="Help", menu=menuHelp)

        window.config(menu = menuBar)

    def configureWindow(self, window):

        # on change la taille de la fenetre pour qu'elle prenne tout l'écran
        screenHeight = self.winfo_screenheight() - 70
        screenWidth = self.winfo_screenwidth()
        window.geometry(str(screenWidth) + "x" + str(screenHeight))
        # on empeche le changement de taille de la fenetre
        window.resizable(width=False, height=False)

    