```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Basic filter for integers
values1 = [3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, List)
assert all(isinstance(x, int) for x in result1)

# Test case 2: Filter empty list
values2 = []
result2 = filter_integers(values2)
assert isinstance(result2, List)
assert not any(isinstance(x, int) for x in result2)

# Test case 3: Filter list with non-integer
values3 = [1, 2, 3, 'abc', {}, [])
result3 = filter_integers(values3)
assert isinstance(result3, List)
assert all(isinstance(x, int) for x in result3)
```