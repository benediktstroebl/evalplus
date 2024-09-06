Here's a self-contained Python script with a function that filters out integers from a list of various types:
```python
from typing import List, Any

def filter_integers(values:
    """
    filtered_int: List[int] = []

    for val in values:
        if isinstance(val, (int, float)):
            filtered_int.append(val)

    return filtered_int
```

This function uses the `isinstance` function to check if the value is an integer or a float, and then adds it to the `filtered_int` list.  The example is provided: you can add more test cases to verify the function's behavior.