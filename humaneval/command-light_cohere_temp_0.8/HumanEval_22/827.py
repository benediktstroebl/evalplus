```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3
print(filter_integers([10, 20, 'hello', 40, 50]))  # [10, 20, 40]

# Test case 4
print(filter_integers([1, 2, 'three', 3, 4, 'five']))  # [1, 2]
```