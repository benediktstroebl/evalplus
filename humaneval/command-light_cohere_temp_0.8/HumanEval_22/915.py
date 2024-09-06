```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [num for num in values if isinstance(num, int)]

# Testing the function with known good inputs/outputs
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 'aa', 3, 'abc'])))  # ['1', '2', 'aa', 3]
print(filter_integers([1, 2, 3.ATOR]))  # []
```