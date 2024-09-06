from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # your code here
    # convert numbers to a list of strings
    numbers = numbers.split()

    # convert list of strings to a list of ints
    numbers = [int(s) for s in numbers]

    # sort the list of ints
    numbers.sort()

    # convert list of ints to a list of strings
    numbers = [str(s) for s in numbers]

    # convert list of strings to a string
    numbers =''.join(numbers)

    return numbers

