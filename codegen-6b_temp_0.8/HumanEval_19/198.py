from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return ("".join(sorted(numbers)))


import pytest
from solutions.kyu_7.sort_numbers import sort_numbers

EXAMPLES = (
    ("one two three four five six seven eight nine", "one two three four five six seven eight nine"),
    ("0 three 1 one 1", "0 1 1 3"),
    ("", ""),
)

