from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    result = []
    for char in numbers:
        if char == 'zero':
            result.append('0')
        elif char == 'one':
            result.append('1')
        elif char == 'two':
            result.append('2')
        elif char == 'three':
            result.append('3')
        elif char == 'four':
            result.append('4')
        elif char == 'five':
            result.append('5')
        elif char == 'six':
            result.append('6')
        elif char == 'seven':
            result.append('7')
        elif char == 'eight':
            result.append('8')
        elif char == 'nine':
            result.append('9')

    return ''.join(result)
