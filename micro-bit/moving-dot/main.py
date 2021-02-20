from microbit import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class MovingDot:
    __left = {
        UP: LEFT,
        DOWN: RIGHT,
        LEFT: DOWN,
        RIGHT: UP
    }

    __right = {
        UP: RIGHT,
        DOWN: LEFT,
        LEFT: UP,
        RIGHT: DOWN
    }

    def __init__(self):
        self.x = 2
        self.y = 2
        self.direction = UP

    def __ensure_coord(coord):
        if coord < 0:
            return 4
        if coord > 4:
            return 0
        return coord

    def move(self):
        if self.direction == UP:
            self.y -= 1
        elif self.direction == DOWN:
            self.y += 1
        elif self.direction == LEFT:
            self.x -= 1
        elif self.direction == RIGHT:
            self.x += 1

        self.x = MovingDot.__ensure_coord(self.x)
        self.y = MovingDot.__ensure_coord(self.y)

    def turn_left(self):
        self.direction = MovingDot.__left[self.direction]

    def turn_right(self):
        self.direction = MovingDot.__right[self.direction]


dot = MovingDot()

while True:
    if button_a.was_pressed():
        dot.turn_left()
    if button_b.was_pressed():
        dot.turn_right()
    dot.move()

    display.set_pixel(dot.x, dot.y, 1)
    sleep(1000)
    display.clear()
