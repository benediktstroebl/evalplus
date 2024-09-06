```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are choice between 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

    test_sort_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    test_numbers = "three one five"
    assert sort_numbers(test_numbers) == "one three five"
```