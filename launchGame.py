# Compatibility with Python 2 and 3
try:
    import tkinter
    from tkinter import *
except ImportError:
    import Tkinter as tkinter
    from Tkinter import *
# Other imports
import os
# Import other files from the game
import Menus.selectLevel as selectLevel
import Menus.settings as settings
import Menus.about as about
import music

# Main window initialization
mainWindow = tkinter.Tk()

# Screen informations
screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

# Functions definition ----------------------------------------------------------------------------------------------------
def close():
    """Close the main window."""    
    mainWindow.destroy()

def openLevels():
    """Open the levels window."""    
    selectLevel.levelsWindow()

def openSettings():
    """Open the settings window."""    
    settings.settingsWindow()

def openAbout():
    """Open the about window."""    
    about.aboutWindow()

def onEnter(e):
    """On enter event.
    Args:
        e (event): Event.
    """    
    e.widget['bg'] = '#c59dd1'
    e.widget['fg'] = 'white'
    music.playSound('hover', music.getVolume())

def onLeave(e):
    """On leave event.
    Args:
        e (event): Event.
    """ 
    e.widget['bg'] = '#B78BC4'
    e.widget['fg'] = 'white'

# Main window ----------------------------------------------------------------------------------------------------
# Main window setting
mainWindow.title("Traffic Light")
mainWindow.config(background='#B78BC4')
mainWindow.attributes('-fullscreen', True)

# Title
title_icon = PhotoImage(file="./Menus/Assets/Images/traffic_lights.png")
title = Canvas(mainWindow, width=screenWidth*0.7, height=screenHeight*0.35, bg='#B78BC4', bd=0, highlightthickness=0)
title.create_image(screenWidth*0.35, screenHeight*0.2, image=title_icon)
title.pack(side='top')

# Exit button
exitIcon = PhotoImage(file='./Menus/Assets/Images/exit_icon.png', width=round(screenWidth*0.07), height=round(screenHeight*0.1))
exitButton = Button(mainWindow, image=exitIcon, bd=0, bg='#B78BC4', highlightthickness=0, cursor="hand2", activebackground="#c59dd1", command=close)
exitButton.pack()
exitButton.place(x=screenWidth-round(screenWidth*0.07), y=screenHeight - round(screenHeight*0.1))
exitButton.bind("<Enter>", onEnter)
exitButton.bind("<Leave>", onLeave)

# Levels Button
levelsButton = Button(mainWindow, text="Niveaux", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006), command= openLevels)
levelsButton.pack(side='top')
levelsButton.bind("<Enter>", onEnter)
levelsButton.bind("<Leave>", onLeave)

# Setting Button
settingsButton = Button(mainWindow, text="Paramètres", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.008), command=openSettings)
settingsButton.pack(side='top')
settingsButton.bind("<Enter>", onEnter)
settingsButton.bind("<Leave>", onLeave)

# Credits Button
aboutButton = Button(mainWindow, text="A propos", font=('Arial', round(screenWidth*0.016)), bd=0, relief="flat", activebackground="#c59dd1", cursor="hand2", activeforeground="white", bg='#B78BC4', fg="#ffffff", width=round(screenWidth*0.006),  command=openAbout)
aboutButton.pack(side='top')
aboutButton.bind("<Enter>", onEnter)
aboutButton.bind("<Leave>", onLeave)

# Play music
music.playSound('music', music.getVolume())

# Compiling window
mainWindow.mainloop()
