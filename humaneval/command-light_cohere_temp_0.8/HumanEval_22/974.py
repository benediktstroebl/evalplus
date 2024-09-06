Here's a self-contained Python function that filters out integers from a given list:
```python
from typing import List

def filter_integers(values:
    """ 
    filtered_ints = []
    for val in values:
        if isinstance(val, int):
            filtered_ints.append(val)
    return filtered_ints
```

This function, `filter_integers`, takes a list of values as input and iterates through the list. It checks if each value in the list is an integer using the `isinstance` function, and if so, it appends the integer to a new list, `filtered_ints`. The function returns this filtered list as output.