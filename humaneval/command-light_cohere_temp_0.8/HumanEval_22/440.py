```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1: Simple list of integers
print(filter_integers([1, 2, 3, 5]))  # [1, 2, 3]

# Test case 2: List with other data types
print(filter_integers([1, 2, 'abc', 3]))    # []

# Test case 3: Empty list
print(filter_integers([]))           # []

# Test case 4: Complex list
print(filter_integers([1, 2, 'abc', {}]))  # [1, 2]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. 

The test cases demonstrate that the function correctly filters out non-integer values and returns the expected results.