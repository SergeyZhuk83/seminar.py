# 1. Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.
# *Примеры:* 
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# if b == a * a:
#     print('Да')
# elif b * b == a:
#     print('Да')
# else:
#     print('Нет')


# 2.Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# lst = []
# for i in range(5):
#     x = int(input('Введите число: '))
#     print(x)
# print(max(25, 1, 36, 3, 5))

# 3.Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Введите число: '))
# for i in range(-n, n+1):
#     print(i, end = ', ') # end выдает ответ в одну строку, без него идет в столбец.

# 4.Напишите программу, которая будет принимать на вход дробь
#  и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# n = float(input('Введите число: '))
# if n % 1 != 0:
#     print(int(n % 1 * 10))
# else:
#     print('нет')

# 5.Напишите программу, которая принимает на вход число 
# и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input('Введите число: '))
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 15) and n % 30 != 0:
#     print('Кратно')
# else:
#     print('Не кратно')





