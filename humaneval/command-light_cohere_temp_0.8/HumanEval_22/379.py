```python
from typing import List

def filter_integers(values:
    return [num for num in values if isinstance(num, int)]

# Test the function with known good inputs and expected outputs
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 3, 6, '7', 8]))  # []
print(filter_integers([1, 2, '3', 7]))  # []
```