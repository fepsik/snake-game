from turtle import Turtle
SNAKE_STARTING_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.head.color('blue')
        # self.head.shape('triangle')

    def create_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('white')
        snake.goto(position)
        self.segments.append(snake)

    def create_snake(self):
        for n in range(SNAKE_STARTING_LENGTH):
            self.create_segment((n * -20, 0))

    def move(self):
        snake_length = len(self.segments)
        for seg_num in range(snake_length - 1, 0, -1):
            next_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self):
        self.create_segment(self.segments[-1].pos())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
