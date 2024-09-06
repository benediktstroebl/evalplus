```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort()

    test_numbers = "three one five six eight nine"
    assert sort_numbers(test_numbers) == "one three five six eight nine"
    return "Passed tests"

print(sort_numbers("three one five"))
```