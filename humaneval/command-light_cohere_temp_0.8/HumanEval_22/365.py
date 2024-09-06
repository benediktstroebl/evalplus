```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> returns [list of] integers
    """
    return [i for i in values if isinstance(i, int)]

# Test
test_values = [1, 2, '3', 'abc', 3.14, 5]
print(filter_integers(test_values))  # Output: [1, 2, 3, 3.
```