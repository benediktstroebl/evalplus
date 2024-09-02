from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a list of numbers from the input string
    numbers = [int(n) for n in numbers.split()]
    # Sort the list of numbers in ascending order
    numbers.sort()
    # Convert the sorted list of numbers back to a string and return it
    return str(numbers)

