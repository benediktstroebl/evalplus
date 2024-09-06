from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    lower_limit = 1
    upper_limit = 9
    numbers_as_int = [int(i) for i in numbers.split(' ')]
    numbers_as_int.sort()
    return ' '.join([str(i) for i in numbers_as_int])

