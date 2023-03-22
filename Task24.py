# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов.

n = int(input())
lst = list()
for i in range(n):
    x = int(input())
    lst.append(x)

lst_count = list()
for i in range(len(lst)-1):
    lst_count.append(lst[i-1] + lst[i] + lst[i+1])
lst_count.append(lst[-2] + lst[-1] + lst[0])
print(max(lst_count))
