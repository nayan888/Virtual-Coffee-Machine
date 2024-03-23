from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create Menu, CoffeeMaer and MoneyMachine instance
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# start the machine
is_on = True
while is_on:
    # receive user choice
    choice = input(f"​What would you like? ({my_menu.get_items()}): ")
    if choice == 'off':
        is_on = False   # turn off the machine
    elif choice == 'report':
        # print resource and balance report 
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)
