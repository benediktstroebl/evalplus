```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of values 
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Filter integers from a list of mixed data 
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3: Filter integers from empty list 
print(filter_integers([]))  []
```