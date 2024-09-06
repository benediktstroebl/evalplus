```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers)

def test_sort_numbers() -> None:
    """Tests the sort_numbers function
    >>> test_sort_numbers('three one five')
    'one three five'
    """
    assert sort_numbers('three one five') == 'one three five'
```