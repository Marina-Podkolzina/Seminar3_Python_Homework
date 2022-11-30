#. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5.0, 10.01] => 0.19 
# (максимальное значение у числа 1.2 , минимальное у 10.01)


print ("Задайте размер списка:")
n = int(input())
a = [0]*n
for i in range(len(a)):
    print (f'Заполните ячейку № {i}')
    a[i] = input()
print(a)
b = [float(x) for x in a]
for i in range(0, len(a)):
    b[i] = int(b[i]//1)

str = ''
e = 1
count = 0
i = 0
while i < len(a):
    if b[i] < 10*e:
        for j in range(count+2, len(a[i])):
            str = str + a[i][j]
        b[i] = '0.' + str
        str = ''
        i += 1
        count = 0
    else:
        e *= 10
        count += 1
mass = [0]*n
for i in range(0, len(a)):
    if b[i] != '0.':
        mass[i] = b[i]
    else:
        mass[i] = 0
mass1 = [float(x) for x in mass]
max = 0
maxindex = 0
min = 1
minindex = 0
dif = 0

for i in range(0, n):
    if mass1[i] != 0:
        if mass1[i] > max:
            max = mass1[i]
            maxindex = i
        if mass1[i] < min:
            min = mass1[i]
            minindex = i
dif = f'{(max-min):g}' 

print(f'Заданный список: \n {a}')
print("Разница между максимальным и минимальным значением дробной части элементов:")
print(f'{dif} (Максимальное значение у числа {a[maxindex]} , минимальное у {a[minindex]})')

