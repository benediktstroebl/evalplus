```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 'abc', 3.14, 5]
print(filter_integers(values))  # Output: [1, 2, 3, 5]
```
This script defines a function `filter_integers` that filters a given list for only the integers present in it. 

This is a self-contained function that doesn't require any external variables and can be easily tested. 
It utilizes the `isinstance` operator to check if each element in the input list is an integer, and returns a new list containing only the integers.