Here's a self-contained Python function that finds the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in a list of strings.
    """
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in the list, using the `max()` function and the `len` built-in function to get the length of each string.

This function is self-contained and does not require any external modules or functions.