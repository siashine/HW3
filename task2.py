# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = []
len_ls = int(input('Введите длину списка: '))
for i in range(len_ls):
 a.append(int(input(f'Введите {i + 1} число: ')))
print(a)

newArr = []
for j in range(int(len_ls / 2)):
 newArr.append(a[j] * a[-j - 1])
if len_ls % 2 != 0:
 newArr.append(a[j + 1]**2)
print(newArr)