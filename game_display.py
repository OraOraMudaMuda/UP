from tkinter import Frame, Label, CENTER, messagebox, Canvas
import tkinter as tk


import game_functions

EDGE_LENGTH = 400
CELL_COUNT = 4
CELL_PAD = 10

UP_KEY = "'w'"
DOWN_KEY = "'s'"
LEFT_KEY = "'a'"
RIGHT_KEY = "'d'"
R_KEY = 'r'

LABEL_FONT = ("Verdana", 40, "bold")

GAME_COLOR = "#a6bdbb"

EMPTY_COLOR = "#8eaba8"

TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
               32: "#17e650", 64: "#17c246", 128: "#149938",
               256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
               2048: "#031f0a", 4096: "#000000", 8192: "#000000", }

LABEL_COLORS = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
                32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
                256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
                2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0", }

class Display(Frame):
    def __init__(self):
        global okno
        Frame.__init__(self)

        self.pack(anchor='center')
        self.master.geometry("850x800")
        self.master.title('2048')
        self.master.bind("<Key>", self.key_press)

        self.commands = {UP_KEY: game_functions.move_up,
                         DOWN_KEY: game_functions.move_down,
                         LEFT_KEY: game_functions.move_left,
                         RIGHT_KEY: game_functions.move_right,
                         R_KEY: game_functions.fixed_move,
                         }

        okno = Frame(self, width=800, height=800, bg='#f0f0f0')

        okno.pack(fill='both', expand=1)

        # Создаем кнопки
        start_button = tk.Button(master=okno, text="Начать игру", command=self.start_game_from_menu)
        start_button.place(relx=0.5, rely=0.3)

        quit_button = tk.Button(master=okno, text="Выйти из игры", command=self.on_exit)
        quit_button.place(relx=0.5, rely=0.5)

        self.mainloop()

    def start_game_from_menu(self):
        okno.destroy()
        self.start_game()

    def start_game(self):
        global win
        self.grid_cells = []
        self.build_grid()
        self.init_matrix()
        self.draw_grid_cells()
        win = Label(self.master, text='Победа \n Вы прошли игру \n Нажмите на любую клавишу\n передвижения, чтобы продолжить', font='Verdana", 40')

    # обработчик нажатия на кнопку выхода
    def on_exit(self):
        if messagebox.askokcancel("Выход", "Хотите выйти из игры?"):
            self.master.destroy()

    def on_newgame(self):
        okno.destroy()
        background.destroy()
        game_functions.schet = 0
        self.start_game()

    def build_grid(self):
        global okno, text, background
        okno = Frame(self, bg='#F0F0F0', width=50, height=50)
        okno.grid(row=0, column=0)
        exit_button = tk.Button(okno, text="Выход", command=self.on_exit)
        exit_button.grid(row=0, column=0, padx=0, pady=5)
        newgame_button = tk.Button(master=okno, text="Новая игра", command=self.on_newgame, width=20, height=2)
        newgame_button.grid(row=0, column=1, padx=273, pady=5)
        text = Label(okno, text='0', font=("Verdana", 20, "bold"), width=5, height=1)
        text.grid(row=0, column=2, padx=0, pady=5)

        background = Frame(self, bg=GAME_COLOR,
                           width=EDGE_LENGTH, height=EDGE_LENGTH)
        background.grid()

        for row in range(CELL_COUNT):
            grid_row = []
            for col in range(CELL_COUNT):
                cell = Frame(background, bg=EMPTY_COLOR,
                             width=EDGE_LENGTH / CELL_COUNT,
                             height=EDGE_LENGTH / CELL_COUNT)
                cell.grid(row=row, column=col, padx=CELL_PAD,
                          pady=CELL_PAD)
                t = Label(master=cell, text="",
                          bg=EMPTY_COLOR,
                          justify=CENTER, font=LABEL_FONT, width=5, height=2)
                t.grid()

                grid_row.append(t)

            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix = game_functions.initialize_game()

    def draw_grid_cells(self):
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                tile_value = self.matrix[row][col]
                if not tile_value:
                    self.grid_cells[row][col].configure(
                        text="", bg=EMPTY_COLOR)
                else:
                    self.grid_cells[row][col].configure(text=str(
                        tile_value), bg=TILE_COLORS[tile_value],
                        fg=LABEL_COLORS[tile_value])
        self.update_idletasks()


    def key_press(self, event):
        key = repr(event.char)

        if key in self.commands:
            win.place_forget()
            self.matrix, move_made, _ = self.commands[repr(event.char)](self.matrix)
            ochko = game_functions.schet
            text['text']=ochko
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False
            if game_functions.pobeda == True:
                win.place(relx=0.5, rely=0.5, anchor='center')
                game_functions.pobeda = False



gamegrid = Display()