"""Показать на экран таблицу умножения в диапазоне,
указанном пользователем. Например, если пользователь
указал 3 и 5, таблица может выглядеть так
3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
.....................................................................................
5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50"""

while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))

        if start > end:
            raise ValueError

        for i in range(start, end + 1):

            for j in range(1, end + 1):
                print(f"{i}  *  {j} = {i  *  j}", end=' ')


            print()

        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите начало и конец диапазона.")
