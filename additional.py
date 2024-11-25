# Необходимо написать игру ("камень ножницы бумага".
# Как) работает игра.Мы запускаем файл. Далее программа
# спрашивает нас, что мы выбираем(игрок) – (камень / ножницы / бумага
# Далее) боту рандомится камень / ножницы / бумага. Затем происходит
# проверка кто выиграл
#
# Решить задачу необходимо используя 4 функции:
#
# 1) получение выбора игрока
# 2) получение выбора бота
# 3) расчет победителя
# 4) функция play в которой идет игра
#
# Дополнительно:
# 1) добавьте возможность сыграть не один раз а несколько
# 2) после завершения игры сделайте вывод кол - ва побед и
# поражений(предусмотрите вариант ничьи)
import random

lists = ['камень', 'ножницы', 'бумага']
rand_list = random.choice(lists)
print(rand_list)


# 1) получение выбора игрока
def choice_player():

    i = 1
    while i > 0:
        item = input('Выберите и введите камень, ножницы, бумага: ')
        if item in lists:
            print('Yes')
            i = 0
        else:
            print('No')
            item_error = input('Желаете продолжить ввод У/N')
            if item_error == 'Y':
                i = 1
            else:
                print('Остановка')
                i = 0


choice_player()