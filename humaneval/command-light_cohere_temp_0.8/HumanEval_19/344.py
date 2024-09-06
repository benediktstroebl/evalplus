```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ', numbers).
    numbers = [map(map(c => str(97 + ord(c)-64)) , numbers)
    numbers = ''.join(numbers)
    numbers = sorted(numbers)
    return numbers

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'

print(test_sort_numbers())
```