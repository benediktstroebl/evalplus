```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases 

values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # Expected Output: [5]

print(filter_integers(values2))  # Expected Output: [1, 2, 3]
```