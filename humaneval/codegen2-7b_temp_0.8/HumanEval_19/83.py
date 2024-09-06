from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.replace(' ', '')
    if numbers == 'one two three four five six seven eight nine'.replace(' ', ''):
        return 'one two three four five six seven eight nine'.replace(' ', '')
    elif numbers == 'nine one two three four five six seven eight'.replace(' ', ''):
        return 'nine one two three four five six seven eight'.replace(' ', '')
    else:
        return''.join(sorted(numbers.split(' '
