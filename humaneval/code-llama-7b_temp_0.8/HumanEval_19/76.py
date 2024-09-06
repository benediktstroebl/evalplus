from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split string to list
    numbers_list = numbers.split()
    # change list to int
    numbers_list_int = [int(item) for item in numbers_list]
    # sort list
    numbers_list_int.sort()
    # change list back to str
    numbers_list_int_str = [str(item) for item in numbers_list_int]
    # join to string
    return ' '.join(numbers_list_int_str)

