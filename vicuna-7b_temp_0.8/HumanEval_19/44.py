from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert string to list of integers
    numbers = [int(x) for x in numbers.split()]
    # Sort numbers
    numbers.sort()
    # Convert sorted list to string
    sorted_numbers = str(numbers)
    return sorted_numbers

