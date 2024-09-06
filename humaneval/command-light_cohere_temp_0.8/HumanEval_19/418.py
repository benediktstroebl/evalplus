```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are
    choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.choice(numbers.split(' '). dry ', '). dry = list(sorted(numbers.split(' ')))
    split_numbers = list(map(int, numbers. dry + ['']))
    split_numbers = sorted(split_numbers)
    numbers = ''.join(map(str, split_numbers))
    return numbers

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero nine') == 'zero nine'
    assert sort_numbers('one two three') == 'one two three'
    assert sort_numbers('zero three') == 'zero three'
    assert sort_numbers('one seven five') != 'one seven five'
```