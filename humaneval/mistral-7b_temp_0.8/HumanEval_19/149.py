from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    for number in numbers_list:
        if number == 'zero':
            numbers_list.remove(number)
            numbers_list.insert(0, '0')
        elif number == 'one':
            numbers_list.remove(number)
            numbers_list.insert(0, '1')
        elif number == 'two':
            numbers_list.remove(number)
            numbers_list.insert(0, '2')
        elif number == 'three':
            numbers_list.remove(number)
            numbers_list.insert(0, '3')
        elif number == 'four':
            numbers_list.remove(number)
            numbers_list.insert(0, '4')
        elif number == 'five':
            numbers_list.remove(number)
            numbers_list.insert(0, '5')
        elif number == 'six':
            numbers_list.remove(number)
            numbers_list.insert(0, '6')
        elif number == 'seven':
            numbers_list.remove(number)
            numbers
