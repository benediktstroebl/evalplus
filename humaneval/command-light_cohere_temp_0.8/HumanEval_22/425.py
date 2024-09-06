Here is a self-contained Python script that solves the problem of filtering integers from a given list of various types:
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

This script defines a function called `filter_integers` that takes a list of values as input. It then iterates through each value in the list and checks if it is an integer using the `isinstance` function. If the value is an type of integer, it gets added to the `filtered_ints` list.