```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

This function uses a list comprehension, iterating over each value in the input list values. It checks if each item is an instance of int using the isinstance() function, and if true, includes it in the int_values list. Finally, it returns the int_values list, which will contain only the integer values from the original input list.