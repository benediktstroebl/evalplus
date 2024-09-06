```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.

    Args:
        values: list of any python value

    Returns:
        list: list of integers
    """
    return [int(val) for val in values if val.isinstance(int)]
```

You can use this function to filter a list of values and return only the integers. This code is self-contained, easy to understand and modify. We used Python's `isinstance()` to ensure the value is an integer. 

You can also use this function to filter lists of data of various types and not just lists of integers.