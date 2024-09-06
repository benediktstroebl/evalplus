from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the string into a list of numbers
    numbers = numbers.split()
    # convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers]
    # sort the list of integers in ascending order
    numbers.sort()
    # convert the list of integers back to a list of strings
    numbers = [str(num) for num in numbers]
    # join the list of strings back into a single string
    return ' '.join(numbers)

