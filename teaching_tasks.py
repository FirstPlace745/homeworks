# 1st Task
"""

1.
На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный треугольник
в соответствии с примером.

n = 3

***
**
*

"""

# n = int(input('Введите натуральное число: '))
#
# for i in range(n):
#     star = '*'
#     print(star * n)
#     n -= 1


# 2nd Task
'''

2. 
Напишите программу, на вход которой даются четыре числа a, b, c и d
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].
Числа 𝑎, b, c и 𝑑 являются натуральными и не превосходят 10, 𝑎≤𝑏, 𝑐≤𝑑.
Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и 
строка таблицы.

a,b,c,d = 7,10,5,6

    5     6
7  35  42
8  40  48
9  45  54
10  50  60

'''

# a, b, c, d = map(int, input('Введите четыре числа: ').split())
#
# if a > 10 or b > 10 or c > 10 or d > 10 or a > b or c > d:
#     print('Попробуйте другие числа')
# else:
#     for i in range(c, d+1):
#         print('  ', i, end="\t")
#     print('')
#     for j in range(a, b+1):
#         print(j, end="\t")
#         for i in range(c, d+1):
#             print(i*j, end="\t")
#         print('')

# 3rd Task
'''

3. 
Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник с высотой равной n, 
в соответствии с примером:

n =  6

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

___________________________
Данные, которые будут подаваться на вход ——> ф-ия input()

'''

# height_triangle = int(input('Введите высоту Вашего треугольника: '))
# loop_count = 0
# lst_for_loop = []
# lst_for_compar = []
# print_lst = []
# cycle_parameter = 0
#
# for i in range(height_triangle):
#     loop_count += 1
#     cycle_parameter += loop_count
#     lst_for_loop.append(cycle_parameter)
#     print("")
#     for j in range(1, lst_for_loop[-1]+1):
#         if j in lst_for_compar:
#             print_lst.clear()
#         elif j not in lst_for_compar:
#             lst_for_compar.append(j)
#             print_lst.append(j)
#             print(print_lst[-1], end=" ")

# 4rd Task
"""

1.
Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого 
равны введенным числам.
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

a,b,c = 59, 59, 59
result —> Равносторонний

"""
# print('Вводите лишь положительные и натуральные числа!')
# a, b, c = (int(input('Введите первое число: ')),
#            int(input('Введите второе число: ')),
#            int(input('Введите третье число: ')))
#
# if a <= 0 or b <= 0 or c <= 0:
#     if a < 0:
#         a = abs(a)
#     elif b < 0:
#         b = abs(b)
#     elif c < 0:
#         c = abs(c)
#     print('Спасибо, что не послушали и Ввели хуйню')
# elif a == b == c:
#     print('Треугольник: Равносторонний')
# elif a == b and a != c or a == b and b != c:
#     print('Треугольник: Равнобедренный')
# else:
#     print('Треугольник: Разносторонний')


# 5th Task
"""

2.
На вход программы подается 3 целых числа. Напишите программу, которая находит серединное значение из этих чисел

a,b,c = 67, 100, 54
result —> 67

"""

# a, b, c = (int(input('Введите первое число: ')),
#            int(input('Введите второе число: ')),
#            int(input('Введите третье число: ')))
#
# if b < a < c or b > a > c:
#     print(a)
# elif a < b < c or a > b > c:
#     print(b)
# elif a < c < b or a > c > b:
#     print(c)


# 6th Task
"""

3.
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При 
смешивании двух основных цветов получается вторичный цвет:

 -если смешать красный и синий, то получится фиолетовый;
 -если смешать красный и желтый, то получится оранжевый;
 -если смешать синий и желтый, то получится зеленый.

Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь 
помимо названий «красный», «синий» или «желтый», 
то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, 
который получится в результате.

a,b = красный, синий
result —> фиолетовый

"""

# print('Введите два основных цвета, которые хотите смешать. На выбор у вас есть три цвета(красный, синий и желтый')
# first_color = input('Введите первый цвет: ')
# second_color = input('Введите второй цвет: ')
#
# if first_color == 'красный':
#     if second_color == 'синий':
#         print('result —> фиолетовый')
#     elif second_color == 'желтый':
#         print('result —> оранжевый')
#     elif second_color == 'красный':
#         print('result -> красный')
# elif first_color == 'синий':
#     if second_color == 'красный':
#         print('result —> фиолетовый')
#     elif second_color == 'желтый':
#         print('result —> зеленый')
#     elif second_color == 'синий':
#         print('result -> синий')
# elif first_color == 'желтый':
#     if second_color == 'красный':
#         print('result —> оранжевый')
#     elif second_color == 'желтый':
#         print('result —> желтый')
#     elif second_color == 'синий':
#         print('result -> зеленый')
# else:
#     print('Что-то пошло не так, проверьте введенные данные и попробуйте снова!')