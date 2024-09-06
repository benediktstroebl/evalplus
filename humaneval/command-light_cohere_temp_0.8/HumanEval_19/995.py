```python
import typing
from typing import List

def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of integers.
    >>> sorted_list = sort_numbers([1,2,3,4,5])
    print(sorted_list)
    """
    return ["".join(str(num) for num in numbers)]

def test_sort_numbers():
    """
    Test the sort_numbers function
    """
    numbers = [1,2,3,4,5]
    expected = [str(num) for num in numbers]
    actual = sort_numbers(numbers)
    assert expected == actual, "Function did not return expected output"

# Run the test suite
test_sort_numbers()
``` 
This script defines a function `sort_numbers` that takes a list of integers and returns a list of their strings, with each integer converted to a string using a list comprehension. The `test_sort_numbers` function contains a test suite for the `sort_numbers` function.  The tests whether code to pass the test suite.