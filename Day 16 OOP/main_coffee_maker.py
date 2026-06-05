from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
drinks_available = coffee_menu.get_items()

print(drinks_available)

x = coffee_menu.find_drink('espresso')
print(x.name)
print(x.ingredients)
print(x.cost)


