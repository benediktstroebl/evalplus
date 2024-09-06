from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_string = numbers.split()
    for index in range(0, len(numbers_string)):
        numbers_string[index] = int(numbers_string[index])
    numbers_string.sort()
    return ' '.join(map(str, numbers_string))

