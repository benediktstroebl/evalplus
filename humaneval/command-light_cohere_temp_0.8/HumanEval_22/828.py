```python
from typing import List
def filter_integers(values):
    """Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Sample test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 'hello', 0]))  # []
print(filter_integers([1, 2, 3, 'abc', float(1.1)]))  # [1, 2, 3]
```
This script provides a function **filter_integers** that filters a given list of any values and returns a new list containing only the integers. 

The test cases demonstrate the behavior of the function with different types of data and values.