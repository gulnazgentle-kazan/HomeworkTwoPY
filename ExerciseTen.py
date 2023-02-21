"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

n = int(input('Введите количество монеток: '))
reshka = 1
orel = 0
count_reshka = 0
count_orel = 0
coin = 1
while coin <= n:
    coin = coin + 1
    if int(input("Введите сторону: ")) == 1:
        count_reshka = count_reshka + 1
    else:
        count_orel = count_orel + 1
if count_reshka >= count_orel:
    print(f'Нужно перевернуть {count_orel} монет')
else:
    print(f'Нужно перевернуть {count_reshka} монет')
