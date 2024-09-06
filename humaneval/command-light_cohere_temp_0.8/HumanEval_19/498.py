```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

    tests = [
        ("zero", "0"),
        ("one", "3"),
        ("two", "13"),
        ("three", "13"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9")
    ]
    for a, b in tests:
        assert sort_numbers(a) == b, f"AssertionError: {a} != {b}"
```