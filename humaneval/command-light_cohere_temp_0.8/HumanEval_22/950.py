```python
from typing import List
def filter_integers(values:
    return [i for i in values if type(i) == int]

# Test the function with known good inputs
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([1, 'abc', 2, 3]))  # Output: []
print(filter_integers([1, 2, 3, 4, 'abc', 1, 2]))  # Output: []
```