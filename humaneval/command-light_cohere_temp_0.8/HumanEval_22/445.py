Here is a self-contained Python script that defines a function `filter_integers` solving the problem you provided:
```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3]]
values2 = [3.14, 5]
print(filter_integers(values1))  # Output: [1, 2, 3]
print(filter_integers(values2))  # Output: [3.14, 5]
```

This script defines a function `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the input list. It uses the generator expression `x for x in values if isinstance(x, int)` to filter only the integers from the list.