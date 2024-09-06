from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the input string into a list of numbers
    # enumerate the list to match the index with the number
    # sort the list by the number itself
    # join the list
    return ' '.join(map(lambda x: x[1], sorted(enumerate(numbers.split()))))

