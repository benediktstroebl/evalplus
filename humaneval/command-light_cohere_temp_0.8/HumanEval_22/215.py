```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers."""
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = [1, 2, 3, 'abc', {}]
test_result = filter_integers(test_values)
assert test_result == [1, 2, 3]

# Test case 2
test_other_values = ['a', 3.14, 5]
test_result = filter_integers(test_other_values)
assert test_result == [5]
```
The function `filter_integers` takes a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the the expected behavior of the function.

This code is self-contained and provides a solution to the problem. It passes the test cases successfully.