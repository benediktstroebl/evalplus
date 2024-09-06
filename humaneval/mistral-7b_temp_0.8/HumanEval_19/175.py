from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # convert the string of numberals to list of numberals
    numbers = numbers.split()
    # sort the list
    sorted_list = sorted(numbers)
    # convert the list back to a string
    sorted_numbers = ' '.join(sorted_list)
    return sorted_numbers

