from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.update_score()
        
        

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 24,'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 24,'normal'))