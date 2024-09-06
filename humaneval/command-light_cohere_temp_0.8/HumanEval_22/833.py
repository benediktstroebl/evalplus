```python
from typing import List
def filter_integers(values):
    """Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function with known correct output
values = [1, 2, 3, 'abc', {}]
print(filter_integers(values) == [1, 2, 3])
```