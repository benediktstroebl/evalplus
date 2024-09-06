```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

This function takes a list of values of any type and returns a list of integers by filtering out any elements that aren't integer types. It uses Python's `isinstance()` function to check if each value in the list is an instance of the `int` class, and if so, appends it to the `result` list. Finally, it returns the `result` list containing only the integer values from the original list.