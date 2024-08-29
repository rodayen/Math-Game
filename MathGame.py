
import random

#initialise game and keep track of score
def start(n):
    score = 0
    mode = input("Select difficulity: 1-Easy, 2-Medium, 3-Hard ")
    for i in range(0, n):
        run = Problem(i).question(mode)
        if run is True:
            score += 1
    print("Your score is: ", score)


# Random Number Generator for the problems
def num_select(mode):
    easy = random.choice(list(range(3, 10)))
    medium = random.choice(list(range(11, 100)))
    hard = random.choice(list(range(101, 1000)))
    if mode == "3":
        return hard    
    elif mode == "2":
        return medium
    else:
        return easy

# Problem Generator
class Problem():
    def __init__(self, question_n) -> None:
        self.question_n = question_n
        return None

    def question(self, mode):
        var1 = num_select(mode)
        var2 = num_select(mode)
        answer = var1 * var2
        user_answer = input(f"{var1} * {var2} = ")
        if user_answer == str(answer):
            return True
        else:
            return False


start(5)