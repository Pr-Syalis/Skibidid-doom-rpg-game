import random
import time
from skibidi import *
from Helpers import *
input("Нажмите ENTER")
name = "Палач рока"
player = name
current_enemy = 0
history()
while True:
    action = input("Выберите действие: \n1 - атака\n2 - тренировка\n3 - Статистика\n4 - Просмотреть следуещего демона\n5 - просмотреть инвентарь\n6 - Магазин\n7 - Казино\n8 - Цель игры")
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == len(enemies):
            print("You Win")
            break    
    elif action == "2":
        training()
        print()
    elif action == "3":
        display_player()
        print()
    elif action == "4":
        display_enemy(current_enemy)
        print()
    elif action == "5":
        display_inventory()
        print()
    elif action == "6":
        shop()
        print()
    elif action == "7":
        earn()
        print()
    elif action == "8":
        bulba()
        print()