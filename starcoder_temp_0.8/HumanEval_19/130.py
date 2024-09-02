from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # this code was given to me by a mentor, and I used it to help me solve this challenge

    # sort_numbers is a function that takes as input a space-delimited string of numbers
    # split the numbers into a list of numbers
    sort_numbers = sorted(numbers.split(" "))

    # join the numbers back together
    sort_numbers = " ".join(sort_numbers)
    return sort_numbers
