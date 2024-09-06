```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers, key=lambda x: x.
    """

    test cases with invalid inputs.
    assert sort_numbers('abc') == []
    assert sort_numbers('z') == []
    assert sort_numbers('9' * 10) == []  # Should be [0,1,2,3,4,5,6,7,8,9]
    assert sort_numbers('five six three') == ['five six three']
```