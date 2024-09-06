from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    try:
        numbers_list = numbers.split()
        numbers_list = sorted(numbers_list)
        return''.join(numbers_list)
    except AttributeError as err:
        print(f'Please enter a valid string (length > 0)')
        raise err

