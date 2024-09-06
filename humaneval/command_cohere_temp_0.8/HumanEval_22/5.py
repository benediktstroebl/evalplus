```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

This function uses a list comprehension, which is a powerful feature in Python for creating new lists by performing operations on each item in the existing list. Here, it is used to filter the given list `values` only to include items that are instances of the integer class. The `isinstance()` function is a built-in Python function that checks if a given object is an instance of a specified class or type. 

The function then returns a list containing only the integer values from the original list.