```python
from typing import List

def filter_integers(values:
    """
    filtered = []
    for val in values:
        if isinstance(val, int):
            filtered.append(val)
    return filtered
```

This function `filter_integers` takes a list of values as input and returns a new list containing only the integers from the input. It does this by iterating through each element in the input list and checking whether it is an integer using the `isinstance` function. The function then creates a new list called `filtered` and adds the integer to it if it is an integer.