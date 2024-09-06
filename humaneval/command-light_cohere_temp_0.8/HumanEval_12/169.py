Here is a self-contained Python script that defines a function `longest()` solving the problem of returning the longest string from a list of strings:

```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in the list. It first checks if the the list is empty, and returns `None` in such cases. It then uses the maximum function with the `len` key to the string and returns the longest one.

This script is self-contained and has no external dependencies. It passes all the therefore test that it is a function that can solve the problem of returning the longest string from a list of strings.