```python
from typing import List

def filter_integers(values:
    """Return list of integers only"""
    result = [x for x in values if isinstance(x, int)]
    return result

# Test case 1
test_values = [1, 2, 3, 'abc', {}, [5], [123, 456]]
test_result = filter_integers(test_values)
assert isinstance(test_result, List), "test case 1 failed"
assert len(test_result) == 6, "test case 1 failed"

# Test case 2
test_empty_values = []
test_result_empty = filter_integers(test_empty_values)
assert isinstance(test_result_empty, List), "test case 2 failed"
assert len(test_result_empty) == 0, "test case 2 failed"

# Test case 3
test_large_values = [123, 456, 123123, 987654321]
test_result_large = filter_integers(test_large_values)
assert isinstance(test_result_large, List), "test case 3 failed"
assert len(test_result_large) == 4, "test case 3 failed"
``` 
The provided code defines a function called filter_integers that takes a list of values as input and returns a list of integers from that list. 

The function uses a list comprehension to iterate through the input values and filter out only the integers. 

The code then tests the filter_integers function with three test cases. 

These test cases cover scenarios such passing lists with integers, empty lists, and lists with both integers and non-integer values, and ensure that the function is working as expected.