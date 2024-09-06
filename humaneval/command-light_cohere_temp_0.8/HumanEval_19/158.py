```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers.split())
numbers.str()
def test_sort_numbers():
    """
    Test case for the sort_numbers function
    """
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('two three five six') == 'three five six'
    assert sort_numbers('nine eight seven six') == 'eight seven six nine'
    assert sort_numbers('zero one three') == 'one three'
    assert sort_numbers('zero two three four') == 'two three four zero'
    assert sort_numbers('zero three eight six') == 'three eight six zero'
    assert sort_numbers('two eight seven five') == 'eight seven five two'
    assert sort_numbers('seven six three') != 'three three two'
    assert sort_numbers('seven seven two') == 'seven seven two'
test_sort_numbers()
```