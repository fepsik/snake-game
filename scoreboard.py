from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

with open('scores.txt') as file:
    current_high_score = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.color('white')
        self.score = 0
        self.high_score = current_high_score
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}. High score: {self.high_score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = -1
        self.update_score()

    def save_high_score(self):
        with open('scores.txt', 'w') as file:
            file.write(str(self.high_score))