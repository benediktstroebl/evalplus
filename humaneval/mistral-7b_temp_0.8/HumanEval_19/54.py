from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # You can do this by iterating over the list and appending to a new list or by using a list comprehension.
    # The list comprehension is more concise and easier to read.
    return ' '.join(sorted(numbers.split(' ')))
