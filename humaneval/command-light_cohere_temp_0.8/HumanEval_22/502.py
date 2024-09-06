```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers."""
    return [x for x in values if isinstance(x, int)]

# Testing the function with known good inputs
print(filter_integers(['a', 3.14, 5]))      # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([3, 'a', 1, 2, 4, 5]))  # []
```