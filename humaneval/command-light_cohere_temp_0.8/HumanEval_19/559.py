```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 
    'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.Qjoin
   ​numbers sorted from smallest to largest, as expected.
    """
    re.split(numbers,
        pass n, [10,9,8,7,6,5,4,3,2,1])
    return ''.join
    return f'{numbers}'.split()

def test_sort_numbers() -> None:
    """Test the sort_numbers function with different input strings."""
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero two three') == 'zero two three'
    assert sort_numbers('one') == ['one']
    assert sort_numbers('two three four five six seven eight nine') == 'two three four five six seven eight nine'
    assert sort_numbers('nine') == ['nine']
    assert sort_numbers(' ten') == ['ten']
    assert sort_numbers('eight seven six') == 'eight seven six'
```