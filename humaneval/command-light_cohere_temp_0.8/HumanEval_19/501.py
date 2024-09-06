```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.

def test_sort_numbers():
    """This function tests the sort_numbers function."""
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero two three') == 'zero two three'
    assert sort_numbers('eight seven six') == 'eight seven six'
    assert sort_numbers('five six three') == 'five six three'
    assert sort_numbers('nine eight seven') == 'nine eight seven'

# Call the function with test data and verify the output
test_sort_numbers()  # Will pass if the function is correct
```