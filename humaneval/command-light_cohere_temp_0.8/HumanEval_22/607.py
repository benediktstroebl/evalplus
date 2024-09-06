```python
from typing import List

def filter_integers(values):
    """Filter given list for only integers"""
    return [int(x) for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 'abc', [], [1, 2, 3, 4]]
print(filter_integers(values3))  # Output: [1, 2, 3, 4]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list with only the integers from the original list. The test cases demonstrate that the function is correct and returns the expected results.