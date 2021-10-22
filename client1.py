#######Conversion of notes in english notacion to  solfège and plays the sound##########################

from tkinter import *
import Buttons


master = Tk()
master.title("Note Conversor")
w = Canvas(master, width=300, height=30)



w.pack()

buttonA = Button(master, text = "From File", command = Buttons.callbackA, anchor = CENTER)
buttonA.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
buttonA_window = w.create_window(0, 5, anchor=NW, window=buttonA)

buttonL = Button(master, text = "Input", command = Buttons.callbackL, anchor = CENTER)
buttonL.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
buttonL_window = w.create_window(75, 5, anchor=NW, window=buttonL)

buttonP = Button(master, text = "Personalize", command = Buttons.callbackP, anchor = CENTER)
buttonP.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
buttonP_window = w.create_window(150, 5, anchor=NW, window=buttonP)

buttonOP = Button(master, text = "Show notes", command = Buttons.callbackOP, anchor = CENTER)
buttonOP.configure(width = 10, activebackground = "#33B5E5", relief = RAISED)
buttonOP_window = w.create_window(225, 5, anchor=NW, window=buttonOP)

mainloop()

    
    



