from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')
    sorted_numbers = []
    for number in numbers:
        if number == 'zero':
            sorted_numbers.append('0')
        elif number == 'one':
            sorted_numbers.append('1')
        elif number == 'two':
            sorted_numbers.append('2')
        elif number == 'three':
            sorted_numbers.append('3')
        elif number == 'four':
            sorted_numbers.append('4')
        elif number == 'five':
            sorted_numbers.append('5')
        elif number == 'six':
            sorted_numbers.append('6')
        elif number == 'seven':
            sorted_numbers.append('7')
        elif number == 'eight':
            sorted_numbers.append('8')
        elif number == 'nine':
            sorted_numbers.append('9')

    sorted_numbers = ' '.join(sorted_numbers)

    return sorted_numbers

