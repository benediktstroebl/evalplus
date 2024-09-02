from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # convert string to list of strings
    numbers_list = numbers.split()
    numbers_list.reverse()

    # build list of numbers in ascending order
    sorted_numbers_list = [x for x in numbers_list if x not in ['zero', 'nine']]
    sorted_numbers_list.sort()

    # join list of numbers to a string
    sorted_numbers = ', '.join(sorted_numbers_list)
    return sorted_numbers
