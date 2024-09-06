```python
from typing import List

def filter_integers(values:
    return [int(el) for el in values if el.isinstance(int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]
values3 = [1, 2, 3]

print(filter_integers(values1))  # [5]
print(filter_integers(values2))  # [1, 2, 3]
print(filter_integers(values3))  # []
```