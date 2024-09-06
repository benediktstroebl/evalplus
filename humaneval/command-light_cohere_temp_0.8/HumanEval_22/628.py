```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers"""
    return [int(x) for x in values if isinstance(x, int)]

# Tests
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([10, 2, 'a', 20, 40, 90]))  # Output: [10, 20, 90]
```