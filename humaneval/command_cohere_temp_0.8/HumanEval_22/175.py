```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [val for val in values if isinstance(val, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It works by creating a new list with the same values as the input list, but checking each value using the `isinstance()` function to see if it is an instance of the `int` class, and only including the values that are integers in the new list.