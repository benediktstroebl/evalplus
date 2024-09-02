from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.replace(' ', '')  # remove leading and trailing spaces
    numbers = [int(n) for n in numbers.split()]  # convert each number to an integer
    numbers.sort()  # sort the numbers in ascending order
    return ' '.join(str(n) for n in numbers)  # join the sorted numbers with a space in between

