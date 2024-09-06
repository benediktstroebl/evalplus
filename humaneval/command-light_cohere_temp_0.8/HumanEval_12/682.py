Here is a self-contained Python script with a function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from the list of strings.
    Parameters: List of strings
    Returns:
      None if the list is empty, otherwise the longest string
    """
    if not strings:
        return None
    return max(strings, key=len)
```

This script defines a `longest` function that takes a list of strings as input and returns the longest string. The function first checks if the list is empty, and if so, it returns `None` to indicate that there are no strings to consider. The function then uses the max function with the `key` argument set to `len` to identify the longest string in the list.