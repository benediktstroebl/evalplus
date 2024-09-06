from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the string on whitespace, then convert the numbers to integers
    numbers_as_ints = [int(i) for i in numbers.split()]

    # Sort the integers
    numbers_as_ints.sort()

    # Convert the integers back to strings, and return the result
    return ' '.join([str(i) for i in numbers_as_ints])

