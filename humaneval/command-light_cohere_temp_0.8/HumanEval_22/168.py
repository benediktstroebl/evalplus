```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with various input values
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
test_result = filter_integers(test_values)
assert test_result == [5, 1, 2, 3]

# Test with invalid input (non-integer value)
test_error = [1, 2, 'a', 3]
with pytest.assert():
    test_result = filter_integers(test_error)
    assert test_result == []
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The test suite contains various test cases, including passing valid integer values and a test with an invalid non-integer value, which should result in an empty list. 
The test is executed using `pytest` to enable assertions and specify the expected behavior of the function.