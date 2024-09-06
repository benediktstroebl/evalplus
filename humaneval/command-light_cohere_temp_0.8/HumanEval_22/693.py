```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3]]
assert filter_integers(values1) == [1, 2, 3]

values2 = [3.14, 5]
assert filter_integers(values2) == [5]

values3 = [1, 2, 3, 'f']
assert len(filter_integers(values3)) == 0  # This should pass
```