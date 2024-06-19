# Lab1
Функция task0

def task0():
    return 4
def task0():: Объявление функции с именем task0. Эта функция не принимает никаких аргументов.
return 4: Возвращает значение 4. Когда эта функция вызывается, она всегда возвращает число 4.
Пример использования:

print(task0())  # Выведет: 4
task0() возвращает 4, и print выводит это значение на экран.
Функция task1

def task1(len_string):
    length = len(len_string)
    return length
def task1(len_string):: Объявление функции с именем task1, которая принимает один аргумент len_string.
length = len(len_string): Использует встроенную функцию len(), чтобы вычислить длину строки len_string и сохраняет результат в переменную length.
return length: Возвращает значение переменной length, которое является длиной строки.
Пример использования:

print(task1("Hello, World!"))  # Выведет: 13
task1("Hello, World!") возвращает длину строки "Hello, World!", которая равна 13, и print выводит это значение на экран.
Функция task2

def task2(number1, operation, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    elif operation == '//':
        result = number1 // number2
    elif operation == '**':
        result = number1 ** number2
    else:
        result = "Непідтримувана операція"

    return result
def task2(number1, operation, number2):: Объявление функции с именем task2, которая принимает три аргумента: number1, operation, и number2.
if operation == '+':: Проверяет, равен ли аргумент operation строке '+'.
result = number1 + number2: Если operation равно '+', вычисляет сумму number1 и number2 и сохраняет результат в переменную result.
elif operation == '-':: Проверяет, равен ли аргумент operation строке '-'.
result = number1 - number2: Если operation равно '-', вычисляет разность number1 и number2 и сохраняет результат в переменную result.
elif operation == '*':: Проверяет, равен ли аргумент operation строке '*'.
result = number1 * number2: Если operation равно '*', вычисляет произведение number1 и number2 и сохраняет результат в переменную result.
elif operation == '/':: Проверяет, равен ли аргумент operation строке '/'.
result = number1 / number2: Если operation равно '/', вычисляет частное от деления number1 на number2 и сохраняет результат в переменную result.
elif operation == '//':: Проверяет, равен ли аргумент operation строке '//'.
result = number1 // number2: Если operation равно '//', вычисляет целочисленное деление number1 на number2 и сохраняет результат в переменную result.
elif operation == '**':: Проверяет, равен ли аргумент operation строке '**'.
result = number1 ** number2: Если operation равно '**', вычисляет number1 в степени number2 и сохраняет результат в переменную result.
else:: Если ни одно из условий не выполнено (т.е. operation не равен ни одному из известных значений), выполняется следующий блок.
result = "Непідтримувана операція": Устанавливает значение переменной result на строку "Непідтримувана операція".
return result: Возвращает значение переменной result.
Пример использования:

print(task2(10, '+', 5))  # Выведет: 15
print(task2(10, '-', 5))  # Выведет: 5
print(task2(10, '*', 5))  # Выведет: 50
print(task2(10, '/', 5))  # Выведет: 2.0
print(task2(10, '//', 5))  # Выведет: 2
print(task2(10, '**', 2))  # Выведет: 100
print(task2(10, '%', 5))  # Выведет: Непідтримувана операція
В каждом из этих примеров функция task2 принимает два числа и операцию, выполняет соответствующую арифметическую операцию и возвращает результат. Если операция не поддерживается, функция возвращает строку "Непідтримувана операція".
Функция task3

def task3(number_list):
    if not number_list:
        return "Список порожній"

    max_value = max(number_list)
    return max_value
def task3(number_list):: Объявление функции с именем task3, которая принимает один аргумент number_list (список чисел).
if not number_list:: Проверяет, пуст ли список number_list. Если список пуст, выполняется следующий блок.
return "Список порожній": Возвращает строку "Список порожній", если список пуст.
max_value = max(number_list): Использует встроенную функцию max(), чтобы найти наибольшее значение в списке number_list, и сохраняет результат в переменную max_value.
return max_value: Возвращает значение переменной max_value.
Пример использования:

print(task3([1, 2, 3, 4, 5]))  # Выведет: 5
print(task3([]))  # Выведет: Список порожній
В первом примере функция task3 принимает список [1, 2, 3, 4, 5], находит наибольшее значение (5) и возвращает его. Во втором примере функция task3 принимает пустой список и возвращает строку "Список порожній".
Полный исправленный код

#task0
def task0():
    return 4

#task1
def task1(len_string):
    length = len(len_string)
    return length

#task2
def task2(number1, operation, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    elif operation == '//':
        result = number1 // number2
    elif operation == '**':
        result = number1 ** number2
    else:
        result = "Непідтримувана операція"

    return result

#task3
def task3(number_list):
    if not number_list:
        return "Список порожній"

    max_value = max(number_list)
    return max_value

# Примеры использования:
print(task0())  # Выведет: 4
print(task1("Hello, World!"))  # Выведет: 13
print(task2(10, '+', 5))  # Выведет: 15
print(task2(10, '-', 5))  # Выведет: 5
print(task2(10, '*', 5))  # Выведет: 50
print(task2(10, '/', 5))  # Выведет: 2.0
print(task2(10, '//', 5))  # Выведет: 2
print(task2(10, '**', 2))  # Выведет: 100
print(task2(10, '%', 5))  # Выведет: Непідтримувана операція
print(task3([1, 2, 3, 4, 5]))  # Выведет: 5
print(task3([]))  # Выведет: Список порожній





