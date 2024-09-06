```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.app(list(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))

# Test
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
``` 
This code defines a function named `sort_numbers` which sorts a given string of numbers. The function accepts a input as a string of numbers separated by spaces, and returns the sorted version of that string. 

The function uses the `app` method from the typing module, which creates a `List` with the numbers from the input string.