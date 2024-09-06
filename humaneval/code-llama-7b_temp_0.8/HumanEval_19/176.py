from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers is None:
        raise TypeError('numbers cannot be None')
    elif not numbers.isdigit():
        raise ValueError('only numbers are allowed in numbers')
    elif len(numbers) == 0:
        return ''

    numbers_list: List[str] = numbers.split()
    numbers_list.sort()
    return ' '.join(numbers_list)
