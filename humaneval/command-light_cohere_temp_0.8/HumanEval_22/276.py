```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'abc', 3.14]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # [1, 2, 3]
print(filter_integers(values2))  # [1, 2, 3]
```
This script provides a self-contained function that filters out any non-integer values from a list, passing all integers back.