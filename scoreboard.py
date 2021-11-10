from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read()[-1])
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.keep_high_score()
            self.score = 0
            self.update_scoreboard()

    def keep_score(self):
        self.score += 1
        self.update_scoreboard()

    def keep_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"\n{self.high_score}")

