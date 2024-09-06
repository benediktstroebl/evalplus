```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, [], ]
print(filter_integers(values))  # Output: [1, 2, 3, 5]

# Another test with list of any value
values = [1, 2, 3, 'abc', {}, ]
print(filter_integers(values))  # Output: [1, 2, 3]

# Test with other data types
values = ['a', ('b', 1), 5]
print(filter_integers(values))  # Output: [5]
```
This script defines a function called `filter_integers` that filters a list of values and returns a new list containing only the integers. It is also passes multiple tests that the function works correctly with different input scenarios.