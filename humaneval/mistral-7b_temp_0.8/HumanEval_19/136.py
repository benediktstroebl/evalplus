from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_as_int = [int(number.split()[0]) for number in numbers.split()]
    sorted_numbers = sorted(numbers_as_int)
    return ' '.join([f'{number}' for number in sorted_numbers])

