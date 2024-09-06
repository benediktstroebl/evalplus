```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    sorted(int(numbers.split(), lambda x: int(x)), reverse=True)
    return ' '.join(map(str, sorted())))

# Tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
test_sort_numbers()
``` 
This code defines a function sort_numbers that sorts a list of numbers in string format from smallest to largest. The numbers are split into integers and passed to the sort function using a lambda function. The resulting sorted numbers are then converted back to a string and joined with spaces, returning the sorted number string.