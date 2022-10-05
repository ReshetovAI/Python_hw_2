# Задача 4

# Реализуйте алгоритм перемешивания списка, без использования встроенных методов
# (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-100, 100))
    return list

n = int(input('Введите количество элементов списка: '))
numbers = list(n)
print("Начальный список: ", numbers)
for i in range (len(numbers)):
    random_num = randint(i, n-1)
    temp = numbers[i]
    numbers[i] = numbers[random_num]
    numbers[random_num] = temp

print("Перемешанный список: ", numbers)
