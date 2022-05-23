# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.

import random
list1 = [random.randint(1, 10) for _ in range(10)]
print(list1)
for el in list1:
    if list1.count(el) == 1:
        print(el, end=' ')

# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

# import random
# list1 = [random.randint(1, 10) for _ in range(10)]
# print(list1)
# counter = 0
# for i in range(len(list1)):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             counter += 1
# print(counter)

# 3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей

# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(C_1) > sum(C_2):
#     print(f"Сумма больше в кортеже - C_1")
# else:
#     print(f"Сумма больше в кортеже - C_2")
# print(f"Минимальный элемент кортежа C_1 - {C_1.index(min(C_1))+1}")
# print(f"Минимальный элемент кортежа C_2 - {C_2.index(min(C_2))+1}")
# print(f"Максимальный элемент кортежа C_1 - {C_1.index(max(C_1))+1}")
# print(f"Максимальный элемент кортежа C_2 - {C_2.index(max(C_2))+1}")

# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

# str1 = ' An apple a day keeps the doctor away'
# lst = list(str1)
# set1 = set(str1)
# dct = {}
# for el_s in set1:
#     dct[el_s] = lst.count(el_s)
# print(dct)

# 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).

# shop = {
#     "торт": {
#         "состав": ['Сливки', 'Коржи', 'Крем'],
#         "цена": 50,
#         "кол-во": 400,
#     },
#     "пироженное": {
#         "состав": ['Крем', 'Основа', "Джем"],
#         "цена": 5,
#         "кол-во": 2000,
#     },
#     "маффин": {
#         "состав": ['Джем', 'Тесто'],
#         "цена": 2,
#         "кол-во": 1000,
#     }
# }
# itogo = 0
# basket = []
# while True:
#     k = 0
#     el = input("Введите, что вы хотите купить - ")
#     while True:
#         pr = input("Что вы хотите узнать (описание, цена, количество, все, 0(ничего)) - ")
#         if pr.lower() == "цена":
#             print(shop[el]["цена"])
#         elif pr.lower() == "описание":
#             print(shop[el]["состав"])
#         elif pr.lower() == "количество":
#             print(shop[el]["кол-во"])
#         elif pr.lower() == "все":
#             print(shop[el])
#         elif pr == "0":
#             break
#     gr = int(input("Сколько грамм хотите взять - "))
#     for d in shop:
#         if el.lower() == d:
#             k = 1
#             while True:
#                 if shop[el]["кол-во"] < gr:
#                     print(f'Нет столько товаров. Осталось {shop[el]["кол-во"]}')
#                 else:
#                     break
#             basket.append(d)
#             shop[el]["кол-во"] -= gr
#             itogo += gr/100*shop[el]["цена"]
#             break
#     if k == 1:
#         print("Товар в корзине")
#     else:
#         print("Такого товара нет. Проверьте правильность введенного названия. ")
#     end = int(input("Закончили покупку? - (1 - да, 0 - нет) "))
#     if end == 1:
#         break
#     else:
#         continue
# print("Ваши покупки - ", basket)
# print(f'Итого по цене - {itogo} рубля.')

# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# # первом списке, так и во втором.
# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = [5, 6, 7, 3, 7, 6]
# print(len(list(set(lst1).intersection(lst2))))

# 7. Напишите программу, демонстрирующую работу try\except\finally
# try:
#     a = 1
#     b = 0
#     c = a/b
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# finally:
#     print("Конец программы")

