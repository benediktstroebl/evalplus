```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function with different data types
values1 = [3.14, 'a', 5]
values2 = [1, 2, 3, 'abc', {}, [], None]

assert filter_integers(values1) == [5]
assert filter_integers(values2) == [1, 2, 3]

```