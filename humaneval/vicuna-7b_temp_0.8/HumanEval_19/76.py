from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a list of the input string
    list_numbers = List(numbers)

    # Remove any spaces from the numbers
    list_numbers = map(int, list_numbers)

    # Sort the numbers in ascending order
    list_numbers.sort()

    # Convert the list to a string with the numbers separated by space
    string_numbers = str(list_numbers)

    return string_numbers