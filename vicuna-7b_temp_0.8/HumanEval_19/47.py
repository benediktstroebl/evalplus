from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split the input string into a list of numbers
    numbers = numbers.split()
    # sort the list of numbers in ascending order
    numbers.sort()
    # join the sorted list of numbers back into a string
    return ' '.join(numbers)
