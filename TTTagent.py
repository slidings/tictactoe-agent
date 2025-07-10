# Tic Tac Toe AI agent with MiniMax Algorithm

from tkinter import *

turn = 'X'  # X starts first
root = Tk()
board = [['_' for _ in range(3)] for _ in range(3)]

def checkWin(board):
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]

    # No winner
    return None


def clickEvent(button, row, col):
    global turn, board
    if button["text"] == "_":
        if turn == 'X':
            button.config(text=turn, state=DISABLED, bg='lightgreen')
            board[row][col] = turn
            if checkWin(board) != None:
                label.config(text=f"{turn} wins!")
                return
            turn = 'O'
        else:
            button.config(text=turn, state=DISABLED, bg='lightblue')
            board[row][col] = turn
            if checkWin(board) != None:
                label.config(text=f"{turn} wins!")
                return
            turn = 'X'

# Instantiate button Widgets and loading into grids
label = Label(root, text="Tic Tac Toe Game")

for r in range(3):
    for c in range(3):
        button = Button(root, text="_", padx=20, pady=18)
        button.grid(row=r, column=c)
        # Reassignment to freeze the current values of b, r, c
        button.config(command=lambda b=button, row=r, col=c: clickEvent(b, row, col))

label.grid(row=4, column=0, columnspan=3)

# To be implemented MiniMax Algorithm Implementation 
class TicTacToeAgent:
    user_symbol = 'X'
    ai_symbol = 'O'

root.mainloop()