from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    split_numbers = numbers.split()
    for index in range(len(split_numbers)):
        if split_numbers[index] not in ('zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine'):
            raise ValueError('{} is not a valid number.'.format(split_numbers[index]))
    return''.join(sorted(split_numbers
