```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test the function with different input values
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', 1.2]))  # []
 # [1, 2, 3]
print(filter_integers([-1, 2, 3, 'a'])))    # [2, 3]
print(filter_integers([1, 2, 'abc'])))    # []
```