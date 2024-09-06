```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 19, 'a', 2, 6]))  # []
print(filter_integers([9, 2, 'b', 3, 6, 4]))  # [3, 6]
```