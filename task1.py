# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

float_num = input('Введите число: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
        print(sum)