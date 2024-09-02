from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.replace(' ', '')
    numbers = numbers.lower()
    numbers = numbers.split(' ')

    for index, number in enumerate(numbers):
        if number not in ['zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine']:
            raise ValueError(f'Invalid number found at index {index}')

    return''.join(sorted(numbers
