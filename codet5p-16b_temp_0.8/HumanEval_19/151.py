from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    split_numbers = numbers.split()
    numbers_list = []
    for num in split_numbers:
        if num == 'zero':
            numbers_list.append('0')
        elif num == 'one':
            numbers_list.append('1')
        elif num == 'two':
            numbers_list.append('2')
        elif num == 'three':
            numbers_list.append('3')
        elif num == 'four':
            numbers_list.append('4')
        elif num == 'five':
            numbers_list.append('5')
        elif num =='six':
            numbers_list.append('6')
        elif num =='seven':
            numbers_list.append('7')
        elif num == 'eight':
            numbers_list.append('8')
        elif num == 'nine':
            numbers_list.append('9')
    return''.join(numbers_list)

