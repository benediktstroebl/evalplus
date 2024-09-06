from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    split_numbers = numbers.split(' ')
    sorted_numbers = sorted(split_numbers)
    sorted_numbers = [number for number in sorted_numbers if number!= '']
    return''.join(sorted_numbers)

