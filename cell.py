class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self._win:
            if self.has_left_wall:
                self._win.draw_line(self._x1, self._y1, self._x1, self._y2, "white")
            else:
                self._win.draw_line(self._x1, self._y1, self._x1, self._y2, "black")
            if self.has_right_wall:
                self._win.draw_line(self._x2, self._y1, self._x2, self._y2, "white")
            else:
                self._win.draw_line(self._x2, self._y1, self._x2, self._y2, "black")
            if self.has_top_wall:
                self._win.draw_line(self._x1, self._y1, self._x2, self._y1, "white")
            else:
                self._win.draw_line(self._x1, self._y1, self._x2, self._y1, "black")
            if self.has_bottom_wall:
                self._win.draw_line(self._x1, self._y2, self._x2, self._y2, "white")
            else:
                self._win.draw_line(self._x1, self._y2, self._x2, self._y2, "black")

    def _get_center(self):
        return ((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        if self._win:
            self._win.draw_line(
                self._get_center(),
                to_cell._get_center(),
            )
