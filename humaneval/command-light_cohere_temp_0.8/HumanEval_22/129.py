```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

values = ['a', 3.14, 5]
print(filter_integers(values))  # Output: [5]

values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Output: [1, 2, 3]

values = [1, 2, 3, 4, 'five', 6]
print(filter_integers(values))  # Output: [1, 3, 4, 'five', 6]

values = List(range(10))
print(filter_integers(values))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```