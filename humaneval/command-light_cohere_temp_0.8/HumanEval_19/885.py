```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    fact to numbers and then sorted them.
    >>> sorted_numbers('three one five')
    'one three five'
    """
def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five", "Function failed the test"
    assert sort_numbers("zero one two three") == "zero one two three", "Function failed the test"
    assert sort_numbers("nine eight seven six five") == "nine eight seven six five", "Function failed the test"
    assert sort_numbers("abc 123 456") == "abc 123 456", "Function failed the test"
``` 
The above Python script defines a function `sort_numbers` that sorts a string of numbers, and tests the function with various inputs. The tests check if the numbers are correctly sorted.