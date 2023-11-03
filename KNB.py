import random

var = ["Камень", "Ножницы", "Бумага"]
player_win = [["Камень", "Ножницы"], ["Ножницы", "Бумага"], ["Бумага", "Камень"]]
comp_win = [["Ножницы", "Камень"], ["Бумага", "Ножницы"], ["Камень", "Бумага"]]

game = True

while game:
    round = []
    player_move = input('Введите свой выбор - "Камень", "Ножницы" или "Бумага": ')
    if player_move not in var:
        print("Вы ввели недопустимое значение, попробуйте снова")
        continue

    round.append(player_move)
    round.append(random.choice(var))
    print(round)

    if round in player_win:
        print("Player WIN")
    elif round in comp_win:
        print('Comp WIN')
    else:
        print("Ничья")

    print()

    resume = input("Введите Да, если хотите продолжить: ")
    if resume.lower() != 'да':
        print("Были рады с Вами поиграть, всего хорошего")
        game = False
