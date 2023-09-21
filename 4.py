x = int(input('Введите число: '))

factorial = 1

for i in range(1, x + 1):
    factorial *= i
print(factorial)