```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are expected are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    return "Sorted numbers are: " + numbers + "."

def test_sort_numbers() -> None:
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero eight seven') == 'zero eight seven'
    assert sort_numbers('six three nine') == 'six three nine'
    assert sort_numbers('nine') == 'nine'
    assert sort_numbers('one') == 'one'
    assert sort_numbers('two three four') == 'two three four'
    return
```