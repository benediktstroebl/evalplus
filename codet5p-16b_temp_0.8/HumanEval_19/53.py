from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers = numbers.replace(' ', '')  # remove spaces
    numbers = numbers.split(' ')  # split into list of string numbers
    numbers = [int(i) for i in numbers]  # convert all to integers
    numbers.sort()  # sort in ascending order
    numbers = [str(i) for i in numbers]  # convert integers back to strings
    return''.join(numbers)  # join into space-delimited string

