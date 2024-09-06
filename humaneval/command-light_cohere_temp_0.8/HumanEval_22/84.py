Here is a self-contained Python script that solves the problem of filtering integers from a list of various types of values:

```python
from typing import List
from typing import Any

def filter_integers(values:
    filtered = [Any]
    for val in values:
        if isinstance(val, int):
            filtered.append(val)
    return filtered
```

This script provides a solution to the given problem. It utilizes a type hint feature in Python using the `isinstance` function to filter out non-integer values from the `values` list and stores the filtered integers in a new list `filtered`. The function returns this filtered list.