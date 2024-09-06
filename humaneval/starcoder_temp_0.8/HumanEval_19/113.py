from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # convert input string to a list of numbers
    numbers_as_list = numbers.split()

    # sort the list of numbers using the built-in sort() function
    numbers_as_list.sort()

    # convert list back into a string
    numbers_as_list = " ".join(numbers_as_list)

    return numbers_as_list

