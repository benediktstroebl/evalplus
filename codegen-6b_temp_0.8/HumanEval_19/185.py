from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_dict = {
        'one': 'one',
        'two': 'two',
        'three': 'three',
        'four': 'four',
        'five': 'five',
        'six': 'six',
        'seven': 'seven',
        'eight': 'eight',
        'nine': 'nine'
    }
    numbers_sorted = ' '.join(numeral_dict[x] for x in sorted(numeral_dict, key=numerals.index))
    return numbers_sorted

