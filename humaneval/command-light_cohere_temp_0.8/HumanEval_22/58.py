```python
from typing import List

def filter_integers(values:
    """Return a list of integers from a list of any python values"""
    return [x for x in values if isinstance(x, int)]

# Test the function with a few values
values1 = ['a', 3.14, 5]
assert filter_integers(values1) == [5], "Failed to filter integers"

# Test the function with invalid input types
try:
    values2 = [1, 2, 3, 'abc', {}, []]
    assert False, "Expected list, got {} instead".
```
This Python script defines a function called `filter_integers` that filters out non-integer values from a given list of values. It uses a specific values in the test cases to ensure that the function is working correctly with both valid and invalid inputs.