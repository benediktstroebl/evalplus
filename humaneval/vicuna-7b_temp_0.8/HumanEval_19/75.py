from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the input string into a list of individual numbers
    numbers_list = numbers.split()
    # convert the list to a list of integers
    numbers_list = [int(n) for n in numbers_list]
    # sort the numbers in ascending order
    numbers_list.sort()
    # join the sorted numbers back into a string
    return " ".join(map(str, numbers_list))

