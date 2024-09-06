```python
from typing import List

def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test the function with known good inputs
print(filter_integers([3, 14, 5, 1, 2, 'abc']))  # [3, 5, 1, 2]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, '2', '20', 999]))  # [10, 999]
```