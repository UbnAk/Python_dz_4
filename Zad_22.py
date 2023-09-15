# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# 1 Вариант
# def identical_elements(lst_1, lst_2):
#     set_1 = set(lst_1)
#     set_2 = set(lst_2)
#     result = list(set_1.intersection(set_2))
#     result.sort(reverse=True)
#     print(*result)

# n = '2 4 6 8 10 12 10 8 6 4 2'.split()
# m = '3 6 9 12 15 18'.split()
# identical_elements(n, m)






# 2 Вариант
# import random
# from random import randint
#
# def identical_elements():
#     lst_1 = set([random.randint(1, 10) for i in range(int(input('Сколько элементов будет в 1-ом списке? ')))])
#     lst_2 = set([random.randint(1, 10) for i in range(int(input('Сколько элементов будет в 2-ом списке? ')))])
#     result = list(lst_1.intersection(lst_2))
#     result.sort(reverse=False)
#     print(*result)
#
# identical_elements()