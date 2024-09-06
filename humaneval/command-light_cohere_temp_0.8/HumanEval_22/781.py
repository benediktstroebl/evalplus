```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test the function with various arguments
print(filter_integers(['a', 3.14, 5]))  # ['5']
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([-3, 7, 'string', 123, (1, 2)]))  # [-3, 7]
print(filter_integers([0, 0, -0, 0]))  # [0, 0, -0]
```