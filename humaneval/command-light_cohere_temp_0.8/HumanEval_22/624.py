```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if type(x) == int]

values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, [], None]
print(filter_integers(values))  # Output: [5, 1, 2, 3]
```