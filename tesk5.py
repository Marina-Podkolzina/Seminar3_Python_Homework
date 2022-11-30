#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fib(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def NegaFib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

s = [0]
print ('Задайте число: ')
n = int(input())
for i in range(1, n + 1):
    s.append(Fib(i))
    s.insert(0, NegaFib(i))
print(s)
 