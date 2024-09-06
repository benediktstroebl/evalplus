```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Filter integers from a tuple
print(filter_integers((1, 2, 3, 'abc', {})))  # [1, 2, 3]

# Test case 3: Filter integers from an empty list
print(filter_integers([]))  # []

# Test case 4: Filter integers from a list with strings
print(filter_integers([1, 2, 3, 'abc']))  # [1, 2, 3]
```

This script provides a function called **filter_integers**, which takes a list of values as input and returns a new list that contains only the integers from the input list. It is also includes several test cases to demonstrate the functionality of the function.