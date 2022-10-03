#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
#Пример:
#1 -> 2.0
#2 -> 4.25
# 3 -> 6.62037037037037

from msilib import sequence

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

num = get_squerence(n)
print(num)
print(round(sum(num)))