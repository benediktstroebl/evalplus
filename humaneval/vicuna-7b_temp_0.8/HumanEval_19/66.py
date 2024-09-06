from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert input string to list of strings
    numbers = [int(i) for i in numbers.split()]
    # Sort the list
    numbers.sort()
    # Rejoin the sorted list of strings and return
    return " ".join(map(str, numbers))
