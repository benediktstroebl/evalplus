```python
from typing import List
def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([-3, 'three', 'abc', 1, 2, 'four']))  # [-3, 'three', 'abc']
```