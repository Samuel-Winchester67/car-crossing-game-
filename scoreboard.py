FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1


    def level_label(self):
        self.clear()
        self.color("black")
        self.penup()
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)
        self.goto(-220, 260)
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.level+=1
        self.level_label()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("arial", 25, "normal") )

