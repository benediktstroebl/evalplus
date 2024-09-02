from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    new_numbers = ''
    for x in numbers:
        if x == '0':
            new_numbers = new_numbers + 'zero'
        elif x == '1':
            new_numbers = new_numbers + 'one'
        elif x == '2':
            new_numbers = new_numbers + 'two'
        elif x == '3':
            new_numbers = new_numbers + 'three'
        elif x == '4':
            new_numbers = new_numbers + 'four'
        elif x == '5':
            new_numbers = new_numbers + 'five'
        elif x == '6':
            new_numbers = new_numbers + 'six'
        elif x == '7':
            new_numbers = new_numbers + 'seven'
        elif x == '8':
            new_numbers = new_numbers + 'eight'
        elif x == '9':
            new_numbers = new_numbers + 'nine'
        else:
            pass
    return new_numbers

