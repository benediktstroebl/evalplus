from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # change the input to list, so that we can sort it
    # we need numbers to be in a list
    numbers_list = [int(x) for x in numbers.split()]
    return ' '.join([str(x) for x in reversed(sorted(numbers_list))])

