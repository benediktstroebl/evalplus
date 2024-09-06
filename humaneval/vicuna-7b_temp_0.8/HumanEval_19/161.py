from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # convert string to list of numbers
    numbers_list = numbers.split()

    # convert numbers to integers
    numbers_list_int = [int(number) for number in numbers_list]

    # sort numbers
    numbers_list_int.sort()

    # convert list of integers back to string
    numbers_list_str = [str(number) for number in numbers_list_int]

    # join string of numbers
    return ' '.join(numbers_list_str)

