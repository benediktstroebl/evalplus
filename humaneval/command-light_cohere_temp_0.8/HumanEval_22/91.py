```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with known correct results
print(filter_integers([3.14, 5, 1, 2, 'abc', None]))  # [3, 5, 1, 2]
print(filter_integers(['abc', 'abc', '123')))  # ['abc', '123']
print(filter_integers([1, 2, 3, 'abc', {}]))  # [1, 2, 3]
print(filter_integers([1, 2, 'abc']))  # ['1', 2]
print(filter_integers([1, 2, 3, 'abc', None, 'hello']))  # []
```