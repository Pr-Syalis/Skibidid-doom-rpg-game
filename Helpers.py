import time
import random
from skibidi import *

def fight(current_enemy):
    round = random.randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f"Противник - {enemy['name']}: {enemy['script']}")
    input("Нажмите Enter, чтобы продолжить ")
    print()

    while player["hp"] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f"{player['name']} aтакует {enemy['name']}.")
            crit = random.randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}, {enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        else:
            print(f"{enemy['name']} атакует {player['name']}")
            player['hp'] -= enemy['attack'] * player["armor"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}, {enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f"Противник - {enemy['name']}: {enemy['win']}")
        current_enemy += 1
    else:
        print(f"Противник - {enemy['name']}: {enemy['loss']}")
    player["hp"] = 200
    return current_enemy

def training():
    training_type = input("1 - тренировать атаку, 2 - тренировать оборону ")
    
    skip = "2"
    if items["2"]["name"] in player["inventory"]:
        skip = input("желаете пропустить тренировку? 1 - да, 2 - нет.")
    if skip == "2":
        for i in range(0, 101, 20):
            print(f"Тренировка завершена на {i}%")
            time.sleep(1.5)
        if training_type == "1":
            player['attack'] += 2
            print(f"Тренировка окончена! Теперь атака равна {player['attack']}")
        elif training_type == "2":
            player['armor'] -= 0.09
            print(f"Тренировка окончена! Теперь броня поглощает {100 - player['armor']*100} урона")



def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')

def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')


def display_inventory():
    print("У вас есть")
    for value in player["inventory"]:
        print(value)
    print(f"У вас есть {player['money']}")
    print()
    if "Зелье удачи" in player['inventory']:
        potion = input("Выпить зелье удачи 1 2")
        if potion == "1":
            player["Luck"] += 7
            print(f"{player['luck']}%")
            player['inventory'].remove("Зелье удачи")


def shop():
    print('Добро пожаловать, путник! Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if item in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрёл {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()


def earn():
    print()
    result = random.randint(1, 100)
    time.sleep(1.5)
    print("Результат...")
    time.sleep(1.5)
    print("скибиди")
    time.sleep(1.5)
    if result < 67:
        print("Вы заработали 500 монет")
        player['money'] += 500
    else:
        print("Вы проиграли 500 монет")
        player['money'] -= 500
    print(f"У вас осталось {player['money']}")

def history():
        print("Король новик: Против всех исчадий из глубин преисподней,\n против всех нечестивцев рода людского, против легионов мы выставим тебя одного.")
def bulba():
        print("Цель игры убить 3 жрецов ада и остоновить вторжение демонов на землю")