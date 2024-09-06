from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # remove whitespaces
    numbers = numbers.replace(' ', '')

    # split into a list of strings
    numbers = numbers.split()

    # sort numbers
    numbers.sort()

    # join the sorted list into a string
    numbers = ' '.join(numbers)

    return numbers

