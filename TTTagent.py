# Tic Tac Toe AI agent with MiniMax Algorithm

from tkinter import *

root = Tk()

# Instantiate Label Widgets
label = Label(root, text="Tic Tac Toe Game")
label_11 = Label(root, text="_").grid(row=0, column=0)
label_12 = Label(root, text="_").grid(row=0, column=1)
label_13 = Label(root, text="_").grid(row=0, column=2)
label_21 = Label(root, text="_").grid(row=1, column=0)
label_22 = Label(root, text="_").grid(row=1, column=1)
label_23 = Label(root, text="_").grid(row=1, column=2)
label_31 = Label(root, text="_").grid(row=2, column=0)
label_32 = Label(root, text="_").grid(row=2, column=1)
label_33 = Label(root, text="_").grid(row=2, column=2)



# Alternate: Load label into the window via packing
# label.pack()

class TicTacToeAgent:
    user_symbol = 'X'
    ai_symbol = 'O'

root.mainloop()