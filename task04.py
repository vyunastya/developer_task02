#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел
n = int(input("Введите число N, больше 0 "))
my_list = []
for i in range(-n, n + 1):
    my_list.append(i)
print(my_list)
str = input("Введите номера индексов для перемножения: ") #Ввод корректных индексов
str += ' '
multiplication = 1
start = 0
end = 0
print (str)
for i in range(len(str)):
    if str[i] == ' ':
        end = i
        index = int(str[start:end])
        multiplication *= my_list[index]
        start = end + 1

print(f'Произведение элементов списка равно {multiplication}')