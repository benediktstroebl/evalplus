```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers. sort smaller, spaces, zero to nine"""
    return numbers.

def test_sort_numbers() -> None:
    numbers = "three onefive"
    expected = "one three five"
    actual = sort_numbers(numbers)
    assert actual == expected, "test failed: " + expected + " != " + actual + ")"
```