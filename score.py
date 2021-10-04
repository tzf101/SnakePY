from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.updateScore()
    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score = {self.score}", False, ALIGNMENT, FONT)
    
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over ;-;", False, ALIGNMENT, FONT)
