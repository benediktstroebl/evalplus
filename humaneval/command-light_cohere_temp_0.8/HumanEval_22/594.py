```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers"""
    return [num for num in values if isinstance(num, int)]

# Test the function
test_values = [1, 2, 3, 'abc', 4, 'five', (5)]
result = filter_integers(test_values)
assert len(result) == 6, "Filter returned the wrong length!"

# Test again
test_data = [1, 2, 3, 4, 'five', (6)]
result = filter_integers(test_data)
assert len(result) == 5, "Filter returned the wrong length!"
```