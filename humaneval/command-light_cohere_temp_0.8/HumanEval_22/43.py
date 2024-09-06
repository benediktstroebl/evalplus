```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1
values = ['a', 3.14, 5]
result = filter_integers(values)
assert len(result) == 3, "Error: Filter failed"

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert len(result) == 3, "Error: Filter failed"

# Test case 3
values = List(range(1, 10))
result = filter_integers(values)
assert len(result) == 10, "Error: Filter failed"

# Test case 4
# This is to check the function with non-integer values
values = ['a', 'bc', 2, 3, 4]
result = filter_integers(values)
assert len(result) == 0, "Error: Filter returned non-integer values"
```