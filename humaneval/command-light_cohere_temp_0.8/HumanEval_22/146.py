```python
from typing import List

def filter_integers(values:
    """Return integers only from the given list"""
    return [num for num in values if isinstance(num, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))     # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', '123'])) # []
print(filter_integers([1, 2, 3, 4, 5, 6])) # [1, 2, 3, 4]
print(filter_integers([4, 'four', 5, 6]))  # []
```