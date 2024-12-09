
import random

# Генерація випадкового списку чисел
random_numbers = [random.randint(1, 100) for _ in range(20)]
print("Список чисел:", random_numbers)


# Виклик функції
# result = your_function(random_numbers)
# print("Результат:", result)

# Приклад для функції "Знайти найбільше число"
def find_max(numbers):
    return max(numbers)


def find_even(govno):
    a = 0
    for i in govno:
        if i%2 == 0:
            a = a + 1
    return a

def calculate_sum(hz):
    b = 0
    for i in hz:
        b = b + i
    return b
def filter_above_50(h):
    newlist = []
    lap = 0
    for i in h:
        if i >50:
            newlist.insert(lap, i)
            lap = lap + 1
    return newlist



# Виклик функції
result = find_max(random_numbers)
print("Найбільше число:", result)
print("Додатні ", find_even(random_numbers))
print("Сумма ", calculate_sum(random_numbers))
print("Більше 50 ", filter_above_50(random_numbers))