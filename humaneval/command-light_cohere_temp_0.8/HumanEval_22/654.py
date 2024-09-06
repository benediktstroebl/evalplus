```python
from typing import List
def filter_integers(values): 
    return [i for i in values if isinstance(i, int)]

# Test the function with several inputs
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([3, 'three', 6, 'item']))  # []
print(filter_integers([10, 2, '20', 3, '40']))  # [10, 2]
```