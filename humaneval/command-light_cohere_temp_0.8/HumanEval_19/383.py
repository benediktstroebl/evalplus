Here's the self-contained Python function along with test cases: 

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are array is ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = sorted(numbers.split())
    small_set = set(numbers)
    return ' '.join(sorted(small_set))

# Test cases
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine eight seven six') == 'nine eight seven six'
    assert sort_numbers('five six three') == 'five six three'
    assert sort_numbers('zero nine') == 'zero nine'
    assert sort_numbers('one') == 'one'
    assert sort_numbers('two three four') == 'two three four'
```

This script provides a function to sort a given list of numbers from the smallest to the largest. The test cases aim to validate the function's behavior for different inputs.