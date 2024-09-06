```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, float('inf'), None]
print(filter_integers(values3))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a list comprehension and the `isinstance` check to filter out the integers.