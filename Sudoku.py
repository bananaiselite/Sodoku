from tkinter import *
import datetime

root = Tk()
root.geometry('505x640')


class Launch:

    # Set Title, Grid and Menu
    def __init__(self, master):

        # Title and settings
        self.master = master
        master.title("Sudoku")

        # Front-End Menu
        menu = Menu(master)
        master.config(menu=menu)
        file = Menu(menu)
        level_choice = Menu(file)
        menu.add_cascade(label='File', menu=file)
        file.add_cascade(label='level', menu=level_choice)
        level_choice.add_command(label='easy', command=self.easy_board)
        level_choice.add_command(label='normal', command=self.normal_board)
        level_choice.add_command(label='difficult', command=self.hard_board)
        file.add_command(label='Exit', command=master.quit)

        # Front-End Button
        s = SolveSudoku()
        check_btn = Button(text='check', command=self.solveInput)
        check_btn.place(anchor='sw', x=10, y=560)
        clear_btn = Button(text='clear', command=self.clearAll)
        clear_btn.place(anchor='sw', x=80, y=560)

        # Metadata and utilities
        self.check = True
        self.started = False
        self.currentBoard = []
        for i in range(10):
            self.currentBoard.append([])
            for j in range(10):
                self.currentBoard[i].append(0)
        self.solutionProvider = SolveSudoku()

    def easy_board(self):

        easy = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
                [2, 8, 9, 0, 0, 4, 0, 0, 0],
                [3, 4, 6, 2, 0, 5, 0, 9, 0],
                [6, 0, 2, 0, 0, 0, 0, 1, 0],
                [0, 3, 8, 0, 0, 6, 0, 4, 7],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 7, 8],
                [7, 0, 3, 4, 0, 0, 5, 6, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        font = ('Arial', 28)
        color = 'white'
        px, py = 1, 0

        # Front-end Grid
        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(0, 9):
            for j in range(0, 9):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = 'gray'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(self.master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                           highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                           textvar=savedNumbers[i][j], justify='center')
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j, ipadx=10, ipady=10)
                if easy[i][j] != 0:
                    num = Label(self.master, text=easy[i][j], bg=color, font='Arial 28')
                    num.grid(row=i, column=j)

        self.setCurrentBoard(easy)
        self.started = True
        return easy

    def normal_board(self):

        normal = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
                  [6, 0, 0, 0, 7, 5, 0, 0, 9],
                  [0, 0, 0, 6, 0, 1, 0, 7, 0],
                  [0, 0, 7, 0, 4, 0, 2, 6, 0],
                  [0, 0, 1, 0, 5, 0, 9, 0, 0],
                  [9, 0, 4, 0, 0, 0, 0, 0, 5],
                  [0, 7, 0, 3, 0, 0, 0, 1, 2],
                  [1, 0, 0, 0, 0, 7, 4, 0, 0],
                  [0, 4, 9, 2, 0, 6, 0, 0, 7]]

        font = ('Arial', 28)
        color = 'white'
        px, py = 1, 0

        # Front-end Grid
        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(0, 9):
            for j in range(0, 9):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = 'gray'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(self.master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                           highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                           textvar=savedNumbers[i][j], justify='center')
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j, ipadx=10, ipady=10)
                if normal[i][j] != 0:
                    num = Label(self.master, text=normal[i][j], bg=color, font='Arial 28')
                    num.grid(row=i, column=j)

        self.setCurrentBoard(normal)
        self.started = True
        return normal

    def hard_board(self):

        hard = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]]

        font = ('Arial', 28)
        color = 'white'
        px, py = 1, 0

        # Front-end Grid
        self.__table = []
        for i in range(1, 10):
            self.__table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(0, 9):
            for j in range(0, 9):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'gray'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = 'gray'
                else:
                    color = 'white'

                self.__table[i][j] = Entry(self.master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                           highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                           textvar=savedNumbers[i][j], justify='center')
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j, ipadx=10, ipady=10)
                if hard[i][j] != 0:
                    num = Label(self.master, text=hard[i][j], bg=color, font='Arial 28')
                    num.grid(row=i, column=j)

        self.setCurrentBoard(hard)
        self.started = True
        return hard

    # Correct the Grid if inputs are uncorrect
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() == '':
                    continue
                if len(savedNumbers[i][j].get()) > 1 or savedNumbers[i][j].get() not in ['1', '2', '3', '4', '5', '6',
                                                                                         '7', '8', '9']:
                    savedNumbers[i][j].set('')

    # Clear the Grid
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() != '':
                    savedNumbers[i][j].set('')

                    color = 'white'
                    if (i < 3 or i > 5) and (j < 3 or j > 5):
                        color = 'gray'
                    elif i in [3, 4, 5] and j in [3, 4, 5]:
                        color = 'gray'

                    self.__table[i][j] = Entry(self.master, width=2, font=('Arial', 28), bg=color,
                                                         cursor='arrow',
                                                         borderwidth=0,
                                                         highlightcolor='yellow', highlightthickness=1,
                                                         highlightbackground='black',
                                                         textvar=savedNumbers[i][j], justify='center')
                    self.__table[i][j].grid(row=i, column=j, ipadx=10, ipady=10)
        self.check = True

    # Utils
    def setCurrentBoard(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[i])):
                self.currentBoard[i][j] = bo[i][j]

    def convertToBoard(self):
        board = []
        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(self.currentBoard[i][j])
        return board

    # Calls the class SolveSudoku
    def solveInput(self):
        if self.started and self.check:
            bn = self.convertToBoard()
            bo = self.convertToBoard()
            self.solutionProvider.solve(bo)
            s = SolveSudoku()
            while True:
                find = s.find_empty(bn)
                if not find:
                    break
                bn[find[0]][find[1]] = bo[find[0]][find[1]]
                if savedNumbers[find[0]][find[1]].get() == '':
                    savedNumbers[find[0]][find[1]].set(bo[find[0]][find[1]])
                elif savedNumbers[find[0]][find[1]].get() != str(bo[find[0]][find[1]]):
                    self.mistake(find)


        self.check = False

    def mistake(self, pos):
        bo = self.convertToBoard()
        self.solutionProvider.solve(bo)
        print(pos)
        if savedNumbers[pos[0]][pos[1]].get() != bo[pos[0]][pos[1]] :
            self.__table[pos[0]][pos[1]] = Entry(self.master, width=2, font=('Arial', 28), bg='red', cursor='arrow',
                                       borderwidth=0,
                                       highlightcolor='yellow', highlightthickness=1,
                                       highlightbackground='black',
                                       textvar=savedNumbers[pos[0]][pos[1]], justify='center')
            self.__table[pos[0]][pos[1]].grid(row=pos[0], column=pos[1], ipadx=10, ipady=10)




class SolveSudoku:
    def solve(self, bo):
        find = self.find_empty(bo)
        if not find:
            return True
        else:
            (row, col) = find
            for i in range(1, 10):
                if self.valid(bo, i, (row, col)):
                    bo[row][col] = i

                    if self.solve(bo):  # calling solve on new board
                        return True
                bo[row][col] = 0
        return False

    def valid(self, bo, num, pos):
        """
        :param bo: Board Matrix
        :param num: int
        :param pos:tuple (row ,col)
        :return:
        """

        # check row
        for j in range(len(bo[0])):
            if bo[pos[0]][j] == num and pos[1] != j:
                return False
        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)


# Global Matrix where are stored the numbers
savedNumbers = []
for i in range(1, 10):
    savedNumbers += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9):
    for j in range(0, 9):
        savedNumbers[i][j] = StringVar(root)

app = Launch(root)
root.mainloop()
