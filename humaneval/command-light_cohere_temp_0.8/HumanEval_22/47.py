```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
assert filter_integers(values1) == [5], "Failed to filter integers"

values2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values2) == [1, 2, 3], "Failed to filter integers"

values3 = [1, 2, 3, 4, 5, 'abc', None]
assert filter_integers(values3) == [1, 2, 3, 4, 5], "Failed to filter integers"
```