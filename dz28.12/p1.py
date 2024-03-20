"""Показать на экран все простые числа в диапазоне,
указанном пользователем. Число называется простым,
если оно делится без остатка только на себя и на единицу.
Например, три — это простое число, а четыре нет."""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True




while True:

    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start > end:
            raise ValueError
        for number in range(start, end + 1):


            if is_prime(number):
                print(number)
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите начало и конец диапазона.")
