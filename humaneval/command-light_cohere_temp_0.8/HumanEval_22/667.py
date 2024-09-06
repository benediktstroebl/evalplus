```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3

# Test case 3
values3 = [True, 2, 3, "apple", [1, 2, 3], {4}]
result3 = filter_integers(values3)
assert len(result3) == 3

# Test case 4
values4 = [object()]
result4 = filter_integers(values4)
assert len(result4) == 0
```