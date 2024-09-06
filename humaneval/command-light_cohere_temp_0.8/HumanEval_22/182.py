```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 'three', (1, 2), [1, 2, 3])
values_bad = ['a', 3.14, 5, [1, 2], {'a': 1}]

assert filter_integers(values_good) == [5, 3, 1, 2, 3]
assert filter_integers(values_bad) == []

# Test with type hinting, should fail with TypeError
# (It would be nice to fix the bug in the values_bad list)
try:
    filter_integers(values_bad)  # Will raise TypeError
except TypeError:
    pass  # Don't crash due to an error
```