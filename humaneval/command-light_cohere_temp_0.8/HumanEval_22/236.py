```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],  # Empty list
    ['a', 3, 'four', 5],  # Mixed data
    [1, 2, 3, 'abc', [], []],  # Mixed data with integers and non-integers
    ]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert actual == [x for x in test_case if isinstance(x, int)], f"Test case: {test_case}, expected: {actual}"
```
This code provides a function that filters out integers from a list of any Python objects. It is also includes a test suite that checks the correctness of the filter_integers function for various input scenarios.