```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3]]
values2 = [3.14, 5]
print("Test Case 1: ", values1)  # Output: [1, 2, 3]
print("Test Case 2: ", values2)  # Output: [3.14, 5]
```