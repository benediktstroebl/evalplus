Here is a self-contained Python function that filters out integers from a list of various Python objects:
```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python objects for integers

    Args:
        values: list of any python object (str, int, float, tuple, etc)

    Returns:
        filtered_ints: list of int
    """
    filtered_ints = [x for x in values if isinstance(x, int)]
    return filtered_ints
```

This function accepts a list of any Python object and returns a new list that contains only the integers from the input list. It achieves this by iterating each element in the input list and checking if it's an instance of the int class.