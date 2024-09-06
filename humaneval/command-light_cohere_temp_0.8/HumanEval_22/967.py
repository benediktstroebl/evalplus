```python
from typing import List
def filter_integers(values: 
    return [i for i in values if type(i) == int]

# Test cases
values1 = ['a', 3.14, 5]
assert filter_integers(values1) == [5]

values2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values2) == [1, 2, 3]

values3 = [1, 2, 3, 4, 'five', 6]
assert list(filter_integers(values3)) == [1, 2, 3, 4]

values4 = [1, 2, 3, 4, 'abc', 6, 7]
assert filter_integers(values4) == [1, 2, 3, 4]

values5 = [1, 2, 'three', 3]
with pytest.assert.param for subcase in values5 assert subcase not in filter_integers(values5)
```