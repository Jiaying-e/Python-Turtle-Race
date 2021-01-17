from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_caspar = []
is_race = False

for caspar_index in range(0, 6):
    new_caspar = Turtle(shape="turtle")
    new_caspar.color(colors[caspar_index])
    new_caspar.penup()
    new_caspar.goto(x=-230, y=y_positions[caspar_index])
    all_caspar.append(new_caspar)

if user_bet:
    is_race = True

while is_race:

    for caspar in all_caspar:
        if caspar.xcor() > 230:
            is_race = False
            winning_color = caspar.pencolor()
            if winning_color == user_bet:
                print(f"You've win and the {winning_color} turtle is the winner ")
            else:
                print(f"You've lost, and the {winning_color} turtle is the winner")
        distance = random.randint(1, 15)
        caspar.forward(distance)

screen.exitonclick()




