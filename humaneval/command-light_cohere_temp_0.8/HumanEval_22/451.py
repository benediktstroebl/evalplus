```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', 5, 7, None]
print(filter_integers(values))  # [1, 2, 3, 5, 7]
```