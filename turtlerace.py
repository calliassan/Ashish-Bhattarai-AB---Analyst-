import turtle
from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80 ]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won and the color is {winning_color}")
            else:
                print(f"the winning color is{winning_color} and you loose")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()