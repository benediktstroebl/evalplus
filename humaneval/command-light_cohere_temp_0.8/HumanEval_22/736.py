```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test case 1: Filter integers from a list of any values
print(filter_integers(['a', 3.14, 5]))  # Output: [5]

# Test case 2: Filter integers from a list of strings
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]

# Test case 3: Filter integers from an empty list
print(filter_integers([]))          # Output: []

# Test case 4: Filter integers from a list containing objects
print(filter_integers([1, 2, '3', True, None])) # Output: [1, 2]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It successfully passes all corresponding tests.