from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    x = y = 20
    num_rows = 12
    num_cols = 10
    cell_width = cell_height = 20
    seed = 0
    maze = Maze(x, y, num_rows, num_cols, cell_width, cell_height, seed, win)
    solved = maze.solve()
    if solved:
        print("Solved!")
    else:
        print("Not solved!")
    win.wait_for_close()


main()
