from random import randint


def rand_numb():
    return randint(0, 10)


def guess_the_number():
    x = rand_numb()
    try_numb = 0
    attempt = int(input('Задайте количество попыток: '))
    while try_numb != attempt:
        try:
            n = int(input('Введите ваше число от 0 до 10: '))
        except ValueError:
            print('ТОЛЬКО ЧИСЛА')
            n = int(input('Введите ваше число от 0 до 10: '))
        if n > 10 or n < 0:
            print('ТОЛЬКО ЧИСЛА ОТ 0 ДО 10')
            n = int(input('Введите ваше число от 0 до 10: '))
        elif n > x:
            try_numb += 1
            print('Твоё число больше моего загаданного')
        elif n < x:
            try_numb += 1
            print('Твоё число меньше моего загаданного')
        elif n == x:
            return print('Ты победил!')
    print('Ты превысил число попыток!')


guess_the_number()
