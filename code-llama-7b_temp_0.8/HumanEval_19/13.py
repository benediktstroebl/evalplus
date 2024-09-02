from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    zero = [0]
    one = [1]
    two = [2]
    three = [3]
    four = [4]
    five = [5]
    six = [6]
    seven = [7]
    eight = [8]
    nine = [9]
    numbers_list = []
    numbers_list.extend(zero)
    numbers_list.extend(one)
    numbers_list.extend(two)
    numbers_list.extend(three)
    numbers_list.extend(four)
    numbers_list.extend(five)
    numbers_list.extend(six)
    numbers_list.extend(seven)
    numbers_list.extend(eight)
    numbers_list.extend(nine)

    for index, number in enumerate(numbers):
        if number == 'zero':
            numbers[index] = zero[0]
        elif number == 'one':
            numbers[index] = one[0]
        elif number == 'two':
            numbers[index] = two[0]
        elif number == 'three':
            numbers[index] = three[0]
        elif number == 'four':
            numbers[index] = four[0]
        elif number == 'five':
            numbers[index] = five[0]
        elif number == 'six':
            numbers[index] = six[0]
        elif number == 'seven':
            numbers[index] = seven[0]
        elif number == 'eight':
            numbers[index] = eight[0]
        elif number == 'nine':
            numbers[index] = nine[0]
    numbers.sort()
    string = ''
    for number in numbers:
        string += str(number)
        string += ' '
    string = string[:-1]
    return string

