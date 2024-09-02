from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers == '':
        return ''
    if len(numbers.split()) == 1:
        return numbers
    return sorted([sort_numbers(numbers.split()[i]) for i in range(len(numbers.split()))])

