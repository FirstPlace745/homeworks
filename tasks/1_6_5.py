"""

Дан список с числами:

[-1, 2, -3, 4, 5, 11]
Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.

"""

list_ = [-1, 2, -3, 4, 5, 11]
list2 = []

for i in list_:
    if 10 > i > 0:
        list2.append(i)

print(sum(list2))