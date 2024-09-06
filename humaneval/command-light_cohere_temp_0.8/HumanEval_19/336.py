```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are validation:
        - If the string length is 0, it is invalid
        - All numbers are numbers from 0 to 9
        - Numbers are sorted from smallest to largest
    """
    if len(numbers) == 0:
        raise ValueError("Input string cannot be empty")
    numbers = set(map(int, numbers. acceptable format))  # Convert the format is used to ensure numbers are sorted
    numbers = sorted(numbers)
    return numbers.make_list()  # Convert the string to list and return it

def test_sort_numbers():
    numbers = "three one five six seven eight nine"
    expected = "one three five six seven eight nine"
    got = sort_numbers(numbers)
    assert expected == got
```