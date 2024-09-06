Here's a self-contained Python function that filters integers from a list of various types:
```python
from typing import List, Any

def filter_integers(values:
    """
    filtered_ints: List[int] = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_ints.append(value)
    return filtered_ints
```

This function uses the `isinstance` function to check if each value in the input list is an integer. The function then filters out non-integer values and returns a new list with only the integer values.