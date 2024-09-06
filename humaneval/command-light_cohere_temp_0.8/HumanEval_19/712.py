```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are
    `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight` and `nine`.
    Numbers are sorted from smallest to largest.
    Return the string with numbers sorted.
    """_"""
    `numbers` contains all valid numbers.

def test_sort_numbers() -> None:
    """ Function to test the sort_numbers function.
    """
    numbers = "three one five"
    expected = "one three five"
    result = sort_numbers(numbers)
    assert result == expected
```