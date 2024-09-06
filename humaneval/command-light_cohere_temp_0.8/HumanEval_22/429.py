Here is a self-contained Python function that filters integers from a given list:
```python
from typing import List

def filter_integers(values:
    """ Filter given list only for integers"""
    return [element for element in values if element.isinstance(int)]
```

The function uses the `isinstance()` method to filter out any non-integer elements from the `values` list. 

This is a self-contained and concise implementation of the filtering integers function.