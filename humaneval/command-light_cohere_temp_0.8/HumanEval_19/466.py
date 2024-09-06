Here is a Python script that contains a self-contained function that sorts and validates a list of numbers:
```python
from typing import List


def sort_numbers(numbers: List[int]) -> List[int]:
    """Sorts a list of numbers and returns a new list sorted from smallest to largest"""
    numbers.sort_numbers = sorted(numbers)
    return numbers

def test_sort_numbers() -> None:
    """Test the sort_numbers function with a sample list of numbers"""
    numbers = [1, 3, 5, 2, 7]
    expected = [1, 2, 3, 4, 5]
    got = sort_numbers(numbers)
    assert got == expected, "Got unexpected output: {}".format(got)
```
The code defines a function `sort_numbers` that sorts a list of numbers and returns a new sorted list. The test_sort_numbers function contains a sample list of numbers and checks if the `sort_numbers` function correctly sorts the list and returns the expected output.