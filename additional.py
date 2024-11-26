import random
lists = ['камень', 'ножницы', 'бумага']


def choice_player():
    i = 1
    while i > 0:
        item = input('Выберите и введите камень, ножницы, бумага: ').lower()
        if item in lists:
            return item
        else:
            item_error = input('Ошиблись при вводе, если желаете продолжить \nвведите Да, '
                               'если нет нажмите любую клавишу: ').lower()
            if item_error == 'да':
                i = 1
            else:
                return 'Остановка'


def choice_bot():
    rand_list = random.choice(lists)
    return rand_list


def calculation_winner():
    global z
    player = choice_player()
    bot = choice_bot()
    print('Компьютер выбрал: ', bot)
    if player == bot:
        return 'Ничья'
    elif ((player == 'камень' and bot == 'бумага') or
          (player == 'ножницы' and bot == 'камень') or
          (player == 'бумага' and bot == 'ножницы')):
        return 'Вы проиграли'
    elif player == 'Остановка':
        return 'Вы закончили игру'
    else:
        return 'Вы выиграли'


def play():
    victory = 0
    defeat = 0
    draw = 0
    i = int(input('Введите цифру сколько раз хотите сыграть: '))
    while i > 0:
        rezult = calculation_winner()
        print(rezult)
        if rezult == 'Вы закончили игру':
            i = 0
        elif rezult == 'Вы выиграли':
            victory += 1
            i -= 1
        elif rezult == 'Вы проиграли':
            defeat += 1
            i -= 1
        elif rezult == 'Ничья':
            draw += 1
            i -= 1
        else:
            print('Какая то ошибка!!!!')
    print(f'Вы выграли {victory} раз \nВы проиграли {defeat} раз \nВы сыграли в ничью {draw} раз')


play()
