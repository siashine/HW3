# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def fib(n):
#     a = 0
#     b = 1
#     for __ in range(n):
#         a, b = b, a + b
#     return a

N = int(input('введите число Фибоначчи = '))

Fib = [0, 1]
negaFib = [1]

for n in range(2, N+1):
  f = Fib[n-2] + Fib[n-1]
  Fib.append(f)
  if n%2 == 0:
    negaFib.insert(0, -(f))
  else:
    negaFib.insert(0, f)

FinFib = negaFib + Fib

print(f'{FinFib}')

# def findFib(index):
#     if index == 1:
#         return 0
#     elif index == 2:
#         return 1
#     return findFib(index-1) + findFib(index-2)


# n = int(input(
#     "Введите число:\n"))
# lst = [findFib(i) for i in range(1, n+2)]
# # print(lst)
# lst = lst[::-1] + lst[1:]
# print(lst, '\n')
