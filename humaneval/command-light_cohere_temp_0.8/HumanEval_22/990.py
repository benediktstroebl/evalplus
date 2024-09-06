```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [i for i in values if isinstance(i, int)]

# Test cases
values1 = [1, 2, 'three', 3.14, 5]
print(filter_integers(values1))  # Output: [1, 2, 3, 3.a, 3.2]
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]
values3 = [1, 2, 3, 4, 5]
print(filter_integers(values3))  # Output: [1, 2, 3, 4, 5]
```