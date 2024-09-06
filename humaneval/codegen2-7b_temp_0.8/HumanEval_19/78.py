from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    sorted_numbers = []
    for numeral in numbers:
        if numeral == 'zero':
            sorted_numbers.append('zero')
        elif numeral == 'one':
            sorted_numbers.append('one')
        elif numeral == 'two':
            sorted_numbers.append('two')
        elif numeral == 'three':
            sorted_numbers.append('three')
    return''.join(sorted_numbers
