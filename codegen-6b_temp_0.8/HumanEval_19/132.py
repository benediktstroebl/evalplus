from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')

    def sort_func(number):
        if number == 'zero':
            return 0
        elif number == 'one':
            return 1
        elif number == 'two':
            return 2
        elif number == 'three':
            return 3
        elif number == 'four':
            return 4
        elif number == 'five':
            return 5
        elif number == 'six':
            return 6
        elif number == 'seven':
            return 7
        elif number == 'eight':
            return 8
        elif number == 'nine':
            return 9

    return ''.join([str(number) for number in sorted(numbers, key=sort_func)])

