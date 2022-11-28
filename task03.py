#3 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
n = int(input("Введите число n, больше 0 "))
my_list = []
sum = 0
for i in range(1, n + 1):
    my_list.append((1 + 1/i) ** i)
    sum += my_list[i-1]
print(f'Список: {my_list}')
print(f'Сумма элементов списка равна {sum:.{2}f}')