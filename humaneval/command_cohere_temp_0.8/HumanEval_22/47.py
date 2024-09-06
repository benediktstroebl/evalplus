```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

This function uses a list comprehension that iterates over each value in the input list values. It checks if each item is an instance of int using the isinstance() function. If it is an integer, it includes it in the int_list. Finally, it returns the int_list, which will contain only the integer values from the input list.