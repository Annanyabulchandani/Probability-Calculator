import copy
import random

class Hat:
    def __init__(self, **arwgs):
        self.contents = []
        for k ,v in arwgs.items():
            for i in range(v):
                self.contents.append(k)
    
    def draw(self, draws):
        if draws > len(self.contents):
            return self.contents
        balls = []
        for i in range(draws):
            d = random.randrange(len(self.contents))
            balls.append(self.contents.pop(d))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        exp = new_hat.draw(num_balls_drawn)

        balls_drawn = []
        for k ,v in expected_balls.items():
            for j in range(v):
                balls_drawn.append(k)
        
        match_ball = 0
        for j in balls_drawn:
            if j in exp:
                exp.remove(j)
                match_ball += 1
        
        if match_ball == len(balls_drawn):
            success += 1
        
    if success == 0:
        return 0
    else:
        return success/num_experiments
