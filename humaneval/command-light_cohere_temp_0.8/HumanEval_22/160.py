```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases for function
values1 = [1, 2, 3, 'abc', {}, [5]]
values2 = [3.14, 5]
print(filter_integers(values1))  # [1, 2, 3]
print(filter_integers(values2))  # [3.14, 5]
```