```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [int(x) for x in values if x.isinstance(int)]

# Test case
values = [1, '2', 3, 'abc', {}, [0]]
print(filter_integers(values))  # [1, 2, 3]
```