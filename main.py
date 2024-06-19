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