# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите длину первого списка: '))
arr1 = list(map(int, input().split()[:n]))

m = int(input('Введите длину первого списка: '))
arr2 = list(map(int, input().split()[:m]))

lst = []

for i in set(arr1):
    for j in set(arr2):
        if i == j:
            lst.append(i)

print(sorted(lst))
