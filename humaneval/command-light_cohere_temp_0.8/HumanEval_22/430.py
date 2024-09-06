```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers."""
    return [num for num in values if isinstance(num, int)]

# Test case 1: Filtering [a, 3. son value types list of python objects, not integers.
values = ['a', 3.14, 5]
result = filter_integers(values)
assert len(result) == [5]

# Test case 2: Filtering whitespace values.
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert len(result) == [1, 2, 3]

# Test case 3: Filtering empty list.
values = []
result = filter_integers(values)
assert len(result) == 0
```