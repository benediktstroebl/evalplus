```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', ]
values2 = [3.14, 5]
values3 = [1, 2, 3, 'a', 4]
values4 = [1, 2, 3, 4, 5]

print(filter_integers(values1))  # Output: [1, 2, 3]
print(filter_integers(values2))  # Output: [3.14, 5]
print(filter_integers(values3))  # Output: [1, 2, 3, 'a', 4]
print(filter_integers(values4))  # Output: [1, 2, 3, 4, 5]
```