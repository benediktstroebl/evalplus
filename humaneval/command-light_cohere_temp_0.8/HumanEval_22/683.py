```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test
values_test = [1, 2, 3, 'abc', 47, (()))
assert filter_integers(values_test) == [1, 2, 3]
```