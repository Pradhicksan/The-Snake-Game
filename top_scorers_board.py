import json as js
from turtle import *

FONT = ("Courier", 10, "normal")
ALIGNMENT = "center"


class TopScorers(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-250, 200)
        self.hideturtle()
        self.get_scores()

    def get_scores(self):
        with open('./top_scorers.json', mode='r') as top_scorers_data:
            top_scorers_dictionary = js.load(top_scorers_data)
            self.write(f"{top_scorers_dictionary['1'][0]}: {top_scorers_dictionary['1'][1]}\n"
                       f"{top_scorers_dictionary['2'][0]}: {top_scorers_dictionary['2'][1]}\n"
                       f"{top_scorers_dictionary['3'][0]}: {top_scorers_dictionary['3'][1]}\n"
                       f"{top_scorers_dictionary['4'][0]}: {top_scorers_dictionary['4'][1]}\n"
                       f"{top_scorers_dictionary['5'][0]}: {top_scorers_dictionary['5'][1]}\n", align=ALIGNMENT, font=FONT)

    def update_scores(self, score, user):
        with open('./top_scorers.json', mode='r') as top_scorers_data:
            top_scorers_dictionary = js.load(top_scorers_data)
            # case 1, greater than all previous scores
            if score > top_scorers_dictionary['1'][1]:
                top_scorers_dictionary['5'] = top_scorers_dictionary['4']
                top_scorers_dictionary['4'] = top_scorers_dictionary['3']
                top_scorers_dictionary['3'] = top_scorers_dictionary['2']
                top_scorers_dictionary['2'] = top_scorers_dictionary['1']
                top_scorers_dictionary['1'] = [user, score]

            elif score > top_scorers_dictionary['2'][1]:
                top_scorers_dictionary['5'] = top_scorers_dictionary['4']
                top_scorers_dictionary['4'] = top_scorers_dictionary['3']
                top_scorers_dictionary['3'] = top_scorers_dictionary['2']
                top_scorers_dictionary['2'] = [user, score]

            elif score > top_scorers_dictionary['3'][1]:
                top_scorers_dictionary['5'] = top_scorers_dictionary['4']
                top_scorers_dictionary['4'] = top_scorers_dictionary['3']
                top_scorers_dictionary['3'] = [user, score]

            elif score > top_scorers_dictionary['4'][1]:
                top_scorers_dictionary['5'] = top_scorers_dictionary['4']
                top_scorers_dictionary['4'] = [user, score]

            elif score > top_scorers_dictionary['5'][1]:
                top_scorers_dictionary['5'] = [user, score]

        with open('./top_scorers.json', mode='w') as top_scorers_data:
            js.dump(top_scorers_dictionary, top_scorers_data, indent=4)



