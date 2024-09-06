```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [val for val in values if isinstance(val, int)]

# Tests
values = ['a', 3.14, 5]
test_result = filter_integers(values)
assert test_result == [5]

values2 = [1, 2, 3, 'abc', {}, []]
test_result2 = filter_integers(values2)
assert test_result2 == [1, 2, 3]
``` 

This code provides a function that takes in a list of values and returns a list of integers from those values, with appropriate tests. Would you like to test more cases, or explain any part of this code further?