from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    result = []
    for item in numbers_list:
        if item == 'zero':
            result.append('0')
        elif item == 'one':
            result.append('1')
        elif item == 'two':
            result.append('2')
        elif item == 'three':
            result.append('3')
        elif item == 'four':
            result.append('4')
        elif item == 'five':
            result.append('5')
        elif item == 'six':
            result.append('6')
        elif item == 'seven':
            result.append('7')
        elif item == 'eight':
            result.append('8')
        elif item == 'nine':
            result.append('9')
    result.sort()
    return ' '.join(result)

