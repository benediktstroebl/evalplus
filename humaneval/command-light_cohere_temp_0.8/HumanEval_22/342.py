```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers"""
    return [int(x) for x in values if x.isdigit()]
```
print(filter_integers(['a', 3, 14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([4, 'four', 5]))  # []
```