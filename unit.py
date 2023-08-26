from tkinter import *
import random
import dimension
import configure
import ctypes
import sys


class Cell:
    all = []
    cell_count = configure.cell_count
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_obj = None
        self.is_open = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        Cell.all.append(self)

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg='#414346',
            fg='red',
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines_length == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == configure.mines_count:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations! You won the game!", "Game Over", 0)
        self.cell_button_obj.unbind('<Button-1>')
        self.cell_button_obj.unbind('<Button-3>')

    def create_button_obj(self, location,buttonFont):

        buttonFont=buttonFont
        button = Button(location, width=6, height=2,bg="#414346",font=buttonFont)

        button.bind('<Button-1>', self.left_click_actions)
        button.bind('<Button-3>', self.right_click_actions)
        self.cell_button_obj = button

    def show_mine(self):
        self.cell_button_obj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a Mine", "Play Again", 0)
        sys.exit()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),

            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),

            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_cells_mines_length(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(text=self.surrounding_cells_mines_length)


            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left:{Cell.cell_count}")

            if self.surrounding_cells_mines_length == 0:
                self.cell_button_obj.configure(bg='#414346',fg="white")
            elif self.surrounding_cells_mines_length == 1:
                self.cell_button_obj.configure(bg='#414346',fg="blue")
            elif self.surrounding_cells_mines_length == 2:
                self.cell_button_obj.configure(bg='#414346',fg="dark green")
            else:
                self.cell_button_obj.configure(bg='#414346',fg='red')


        self.is_open = True

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_button_obj.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_button_obj.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, configure.mines_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell{self.x},{self.y}"
