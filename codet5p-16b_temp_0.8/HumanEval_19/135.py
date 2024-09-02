from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    if len(numbers) <= 0:
        return ""
    sorted_numbers = sort_numbers(numbers[1:])
    if int(numbers[0]) <= len(sorted_numbers):
        sorted_numbers = numbers[0] + sorted_numbers
    return sorted_numbers

