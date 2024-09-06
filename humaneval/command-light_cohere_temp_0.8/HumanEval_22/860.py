```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test case 1: basic input
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: list of strings
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3: empty list
print(filter_integers([]))  # []

# Test case 4: empty string
print(filter_integers(''))  # []

# Test case 5: dictionary
print(filter_integers({}"))  # []
```
This script defines a function `filter_integers` that filters a given list of values for integers. It then passes these tests to check if the function is working correctly for different input scenarios.