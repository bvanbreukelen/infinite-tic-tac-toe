import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Infinite Tic Tac Toe")
        self.turn = 'X'
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.moves = {'X': [], 'O': []}
        self.scores = {'X': 0, 'O': 0}
        self.round = 0
        self.create_widgets()

    def create_widgets(self):
        self.turn_label = tk.Label(self.root, text=f"Turn: {self.turn}", font=("Arial", 20))
        self.turn_label.pack(side="top")

        self.score_label = tk.Label(self.root, text=f"Scores - X: {self.scores['X']} O: {self.scores['O']}", font=("Arial", 20))
        self.score_label.pack(side="top")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.buttons = [[tk.Button(self.frame, text="", font=("Arial", 40), width=5, height=2, command=lambda row=row, column=column: self.click(row, column)) for column in range(3)] for row in range(3)]
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].grid(row=row, column=column)
        
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 20), command=self.reset_game)
        self.restart_button.pack(side="top")
        self.restart_button.pack_forget()

    def click(self, row, column):
        if not self.buttons[row][column].cget('text') and len(self.moves[self.turn]) < 4:
            self.board[row][column] = self.turn
            self.buttons[row][column].config(text=self.turn, fg='green' if self.turn == 'X' else 'red')
            self.moves[self.turn].append((row, column))
            if len(self.moves[self.turn]) == 3:
                fade_row, fade_column = self.moves[self.turn][0]
                self.buttons[fade_row][fade_column].config(fg='grey')
            if len(self.moves[self.turn]) == 4:
                remove_row, remove_column = self.moves[self.turn].pop(0)
                self.board[remove_row][remove_column] = None
                self.buttons[remove_row][remove_column].config(text="", fg='black')
                fade_row, fade_column = self.moves[self.turn][0]
                self.buttons[fade_row][fade_column].config(fg='grey')
            if self.check_winner(self.turn):
                self.scores[self.turn] += 1
                self.round += 1
                self.highlight_winner(self.turn)
                messagebox.showinfo("Winner", f"{self.turn} wins this round!")
                self.restart_button.pack(side="top")
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.turn_label.config(text=f"Turn: {self.turn}")
                self.score_label.config(text=f"Scores - X: {self.scores['X']} O: {self.scores['O']}")

    def check_winner(self, player):
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for condition in win_conditions:
            if all(self.board[row][column] == player for row, column in condition):
                self.winning_line = condition
                return True
        return False

    def highlight_winner(self, player):
        for row, column in self.winning_line:
            self.buttons[row][column].config(bg='yellow')

    def reset_board(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.moves = {'X': [], 'O': []}
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", fg='black', bg='SystemButtonFace')

    def reset_game(self):
        self.reset_board()
        self.scores = {'X': 0, 'O': 0}
        self.round = 0
        self.turn = 'X'
        self.turn_label.config(text=f"Turn: {self.turn}")
        self.score_label.config(text=f"Scores - X: {self.scores['X']} O: {self.scores['O']}")
        self.restart_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()