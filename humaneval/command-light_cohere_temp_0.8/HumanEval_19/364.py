```python
from typing import List
def sort_numbers(input_string: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine. 
    Valid choices are
    spaces and numbers.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = input_string.split()
    numbers = [int(num) for num in numbers]
    numbers.sort()
    numbers
    numbers
    return ' '.join(numbers)

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```