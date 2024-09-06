```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

#Test case 1
values1 = [3.14, 'a', 5]
filtered1 = filter_integers(values1)
assert len(filtered1) == 3

#Test case 2
values2 = [1, 2, 3, 'abc', {}, [0])
filtered2 = filter_integers(values2)
assert len(filtered2) == 3

#Test case 3
values3 = [1, 2, 3, 'a', [0, 1, 2, 3])
filtered3 = filter_integers(values3)
assert len(filtered3) == 3
```