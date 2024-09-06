```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [0]]
values2 = [3.14, 5]
assert filter_integers(values1) == [1, 2, 3]
assert filter_integers(values2) == [3, 5]
```