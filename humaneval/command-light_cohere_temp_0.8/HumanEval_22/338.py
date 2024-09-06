```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 'abc', 2, 3, 'five']))  # []
print(filter_integers([9, 2, '10', 3]))    # [9]
print(filter_integers([10, 20, 30, 40, 'for'])) # [30]
```