```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    """
    return numbers

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('five two three') == 'two three five'
    assert sort_numbers('zero one three') == 'one zero three'
    assert sort_numbers('eight seven six') == 'seven six eight'
    assert sort_numbers('six five seven') == 'five seven six'
    assert sort_numbers('nine eight seven') == 'eight seven nine'
    assert sort_numbers('four three six') != 'three six four'
    assert sort_numbers('two one three') != 'one three two'
```