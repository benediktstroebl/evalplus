```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values = [3.14, 5]
result = filter_integers(values)
assert len(result) == 2, "Filter failed"

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert len(result) == 3, "Filter failed"

# Test case 3
values = [1, 2, 3, 'abc', [], [1, 2, 3])
result = filter_integers(values)
assert len(result) == 6, "Filter failed"

print("All tests passed!")
```