from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # convert string to list of numbers
    numbers = [int(number) for number in numbers.split()]
    # sort the list of numbers
    numbers.sort()
    # convert list to string
    return '.'.join(map(str, numbers))

