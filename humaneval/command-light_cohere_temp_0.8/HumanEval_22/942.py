```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test case 1
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3
print(filter_integers([1, 2, 3, 'abc', 123, [1, 2, 3]]))  # [1, 2, 3]
```
This Python script defines a function `filter_integers` that filters a given list of values to include only integers. It uses the critical typing to ensure that the values passed to the function are checked to be of an integer data type.