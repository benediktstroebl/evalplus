from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # return " ".join(sorted(numbers.split()))
    return " ".join(sorted(numbers.split(), key=lambda num: {'one': 0, 'two': 1, 'three': 2, 'four': 3, 'five': 4, 'six': 5, 'seven': 6, 'eight': 7, 'nine': 8, 'zero': 9}[num]))

