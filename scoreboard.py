from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pu()
        self.goto(0, 270)
        self.color("white")
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"SCORE = {self.score} HIGH SCORE = {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
