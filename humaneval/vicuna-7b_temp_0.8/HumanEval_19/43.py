from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of numbers
    numbers = numbers.split()

    # Sort the numbers in ascending order
    numbers.sort()

    # Join the sorted numbers back into a string
    return " ".join(numbers)

