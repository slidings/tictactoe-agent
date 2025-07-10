# Tic Tac Toe AI agent with MiniMax Algorithm

from tkinter import *

root = Tk()

# Instantiate button Widgets and loading into grids
label = Label(root, text="Tic Tac Toe Game")
label_11 = Button(root, text="_", padx=20, pady=18).grid(row=0, column=0)
label_12 = Button(root, text="_", padx=20, pady=18).grid(row=0, column=1)
label_13 = Button(root, text="_", padx=20, pady=18).grid(row=0, column=2)
label_21 = Button(root, text="_", padx=20, pady=18).grid(row=1, column=0)
label_22 = Button(root, text="_", padx=20, pady=18).grid(row=1, column=1)
label_23 = Button(root, text="_", padx=20, pady=18).grid(row=1, column=2)
label_31 = Button(root, text="_", padx=20, pady=18).grid(row=2, column=0) 
label_32 = Button(root, text="_", padx=20, pady=18).grid(row=2, column=1)
label_33 = Button(root, text="_", padx=20, pady=18).grid(row=2, column=2)

# Buttons have attributes that can be disabled (state='disabled') or enabled (state='normal')

# Alternate: Load label into the window via packing
label.grid(row=4, column=0, columnspan=3)

class TicTacToeAgent:
    user_symbol = 'X'
    ai_symbol = 'O'

root.mainloop()