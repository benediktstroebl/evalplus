from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Use a simple O(n) algorithm to sort the numbers
    # We'll get the characters out of numbers in O(1) time, so the total time complexity is O(n)
    return ''.join(sorted(numbers))
    # Alternatively, use a stack to do this in O(n) time

