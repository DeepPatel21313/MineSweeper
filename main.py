from tkinter import *
from unit import Cell
import tkinter.font as font
import configure
import dimension

root = Tk()
root.configure(bg="#0E0E0F")
root.geometry(f'{configure.width}x{configure.height}')

root.title("MineSweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg="#0E0E0F", width=configure.width, height=dimension.height_percentage(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg="#0E0E0F", fg="#FF0014", text="MineSweeper Game", font=('', 50))

centre_frame = Frame(root, bg="#0E0E0F", width=dimension.width_percentage(75), height=dimension.height_percentage(75))
centre_frame.place(x=dimension.width_percentage(30), y=dimension.height_percentage(30))

game_title.place(x=dimension.width_percentage(25), y=0)
buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
for x in range(configure.grid_size):
    for y in range(configure.grid_size):
        c = Cell(x, y)
        c.create_button_obj(centre_frame,buttonFont)

        c.cell_button_obj.grid(column=x, row=y)
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(x=dimension.width_percentage(42), y=dimension.width_percentage(8))
Cell.randomize_mines()
root.mainloop()


