```python
from typing import List
def filter_integers(values:
    return [int(el) for el in values if el.isinstance(int)]

values = [1, 'abc', 3, 'four', []]
print(filter_integers(values))  # Output: [1, 3, 'four']

# Test for other data types too
values = [1, 2, 3, 'abc', {}]
print(filter_integers(values))  # Output: [1, 2, 3]
values = ['a', 3.14, 5]
print(filter_integers(values))  # Output: [5]
```