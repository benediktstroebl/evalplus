```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers"""
    return [num for num in values if isinstance(num, int)]

# Test the function
values = [1, 2, 'three', 3.14, 5]
result = filter_integers(values)
assert len(result) == 5  # should be true
print(result)

```