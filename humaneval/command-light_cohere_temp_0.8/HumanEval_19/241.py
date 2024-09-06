```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = sorted(numbers.split())
    use to cast numbers as a string
    digits = [int(char) for char in numbers]
    numbers = ''.join(''.join(digits)
    return numbers.split()
 use to remove spaces from numbers and convert to list
    return numbers

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers(' six three four') == 'three four six'
    assert sort_numbers('one two three four five six seven eight nine') == 'one two three four five six seven eight nine'
    assert sort_numbers(' eight one three two') == 'one three two eight'
    assert sort_numbers('9 nine') == 'nine nine'
    assert sort_numbers('') == ''
```