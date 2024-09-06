```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.make_list(numbers). hung numbers in the string that begins with zero and ends with nine.

def test_sort_numbers() -> None:
    numbers = ['three onefive', 'zero two seven eight nine']
    expected = 'one three five seven eight nine'
    result = sort_numbers(numbers)
    assert result == expected
    return

test_sort_numbers()
```
This script defines a function `sort_numbers` that takes an input string of numbers separated by spaces and returns a sorted version of the numbers. It also contains a test function that creates a list from a string of numbers separated by spaces and passes it to the `sort_numbers` function.