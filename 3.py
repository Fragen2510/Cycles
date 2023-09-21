x = int(input("Введите число: "))
a = int(input('Введите степень: '))

fin_x = 1

for i in range(a):
    fin_x *= x
print(fin_x)