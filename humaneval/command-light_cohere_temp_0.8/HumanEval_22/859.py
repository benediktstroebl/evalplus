```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [List(['a', 3.14, 5], [1, 2, 'abc', 3], [(), []], [1, 2, 3])

print(filter_integers(test_values))
```