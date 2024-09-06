```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [i for i in values if isinstance(i, int)]

# Test
values1 = [1, 2, 3, 'abc',{},]
values2 = [3.14, 5]
print(filter_integers(values1) == values2)  # True
print(filter_integers([1, 2, 3, 'abc', [], [4]]))  # [1, 2, 3]
print(filter_integers(['a', 3.14]))  # [['a', '1']) # ['1', '3']
```