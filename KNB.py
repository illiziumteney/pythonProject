import random

# Создаем списки просто значений, и выигрышных комбинаций

var = ["камень", "ножницы", "бумага"]
player_win = [["камень", "ножницы"], ["ножницы", "бумага"], ["бумага", "камень"]]
comp_win = [["ножницы", "камень"], ["бумага", "ножницы"], ["камень", "бумага"]]

game = True

# body of game

while game:
    rou = []

# Ход игрока

    player_move = input('Введите свой выбор - "Камень", "Ножницы" или "Бумага": ').lower()
    if player_move not in var:
        print("Вы ввели недопустимое значение, попробуйте снова")
        continue

# Ход NPC

    rou.append(player_move)
    rou.append(random.choice(var))
    print(rou)

# Определяем победителя

    if rou in player_win:
        print("Player WIN")
    elif rou in comp_win:
        print('Comp WIN')
    else:
        print("Ничья")

    print()

# Будем продолжать игру или нет

    resume = input("Введите Да, если хотите продолжить: ")
    if resume.lower() != 'да':
        print("Были рады с Вами поиграть, всего хорошего")
        game = False
