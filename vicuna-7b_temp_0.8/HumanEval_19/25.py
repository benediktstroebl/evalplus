from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the string into a list of strings
    numbers = numbers.split()

    # reverse the order of the list
    numbers.reverse()

    # convert the list of strings back to a string
    numbers_str = ' '.join(numbers)

    # convert the string to a list of numbers
    numbers_list = [int(n) for n in numbers_str.split()]

    # sort the list in ascending order
    numbers_list.sort()

    # join the numbers back into a string
    return ' '.join(str(n) for n in numbers_list)
