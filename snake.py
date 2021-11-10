from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_STEP = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_position()
        self.head = self.segments[0]

    def snake_position(self):  # creates a snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_s = Turtle("square")
        new_s.penup()
        new_s.color("white", "white")
        new_s.goto(position)
        self.segments.append(new_s)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake_position()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):  # Snake constant movement and following of segments
        for s_num in range(len(self.segments) - 1, 0, -1):  # start=2 or len()-1 , stop=0, step=-1 to start from back
            new_x = self.segments[s_num - 1].xcor()
            new_y = self.segments[s_num - 1].ycor()
            self.segments[s_num].goto(new_x, new_y)
        self.head.fd(MOVEMENT_STEP)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
