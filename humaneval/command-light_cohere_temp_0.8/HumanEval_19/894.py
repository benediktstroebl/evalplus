```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split().sort(map(int, numbers. first to_string))

def test_sort_numbers() -> None:
    """ Tests the sort_numbers function.
    numbers = "three one five"
    expected = "one three five"
    result = sort_numbers(numbers)
    assert result == expected, f"Expected {expected}, got {result}"

test_sort_numbers()
```