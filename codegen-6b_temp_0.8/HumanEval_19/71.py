from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_dict = {
        'zero': '',
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
    return " ".join(sorted(numbers.split(), key=lambda x: numbers_dict[x].lower()))

