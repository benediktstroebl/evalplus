```python
from typing import List
def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

#Test cases
values1 = [1, 2, 3, 'abc', 5]
assert filter_integers(values1) == [1, 2, 3]

values2 = [1, 2, 3, 'five', 5]
assert filter_integers(values2) == [1, 2, 3]

values3 = [1, 2, 3, 4]
assert filter_integers(values3) == []

values4 = [1, 2, 4, 5, 'six']
assert filter_integers(values4) == [1, 2, 4]
```