```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, '3', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 5, "Wrong result length"

# Test with complex input
test_data = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(test_data)
assert len(result2) == 4, "Wrong result length"
```