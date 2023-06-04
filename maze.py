from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x,
        y,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        seed=None,
        win=None,
    ):
        self.cells = []
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell = Cell(self._win)
                row.append(cell)
            self.cells.append(row)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self.cells[i][j]
        x1 = self.x + i * self.cell_size_x
        y1 = self.y + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.02)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self.cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0  and not self.cells[i - 1][j].visited:
                to_visit.append((i-1, j))
            if j < self.num_cols - 1 and not self.cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i < self.num_rows - 1 and not self.cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j > 0 and not self.cells[i][j-1].visited:
                to_visit.append((i, j-1))

            if to_visit == []:
                self._draw_cell(i, j)
                return

            next_cell = random.choice(to_visit)

            if next_cell == (i-1, j):
                self.cells[i][j].has_top_wall = False
                self.cells[i-1][j].has_bottom_wall = False
            elif next_cell == (i, j+1):
                self.cells[i][j].has_right_wall = False
                self.cells[i][j+1].has_left_wall = False
            elif next_cell == (i+1, j):
                self.cells[i][j].has_bottom_wall = False
                self.cells[i+1][j].has_top_wall = False
            elif next_cell == (i, j-1):
                self.cells[i][j].has_left_wall = False
                self.cells[i][j-1].has_right_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        # Top
        if i > 0 and i < self.num_rows and self.cells[i - 1][j].visited == False and self.cells[i][j].has_top_wall == False:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i-1][j], True)
        # Right
        if j >= 0 and j < self.num_cols-1 and self.cells[i][j+1].visited == False and self.cells[i][j].has_right_wall == False:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j+1], True)
        # Bottom
        if i >= 0 and i < self.num_rows-1 and self.cells[i+1][j].visited == False and self.cells[i][j].has_bottom_wall == False:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i+1][j], True)
        # Left
        if j > 0 and j < self.num_cols and self.cells[i][j-1].visited == False and self.cells[i][j].has_left_wall == False:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j-1], True)
        return False

       








