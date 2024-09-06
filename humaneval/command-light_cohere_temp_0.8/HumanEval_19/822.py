```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    core number_ 

def test_sort_numbers() -> None:
    input = "three one five"
    expected = "one three five"
    result = sort_numbers(input)
    assert result == expected, f"Expected {expected}, but got {result}"
    return result
```