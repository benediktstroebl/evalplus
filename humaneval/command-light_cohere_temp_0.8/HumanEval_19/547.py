```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split()
 numbers
        return ''.join(sorted(int(num) for num in numbers), reverse=True))

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
 ```