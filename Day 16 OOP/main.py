# object.attribute
# object.method
import prettytable
from prettytable import PrettyTable
import turtle
from turtle import Turtle, Screen

'''
Timmy Section, just trying out different attributes and methods

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

'''

# Using prettytable to create ASCII tables
table = PrettyTable()
table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander"],
    align='l',
)
table.add_column(
    "Type",
    ["Electric", "Water", "Fire"]
)

print(table)
print(type(table))