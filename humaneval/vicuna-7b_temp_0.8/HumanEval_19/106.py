from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a list of strings from the input string
    numbers_list = [numbers]

    # Sort the list in ascending order
    numbers_list.sort()

    # Reverse the list for descending order
    numbers_list.reverse()

    # Convert the list to a string
    numbers_str = ', '.join(numbers_list)

    return numbers_str
