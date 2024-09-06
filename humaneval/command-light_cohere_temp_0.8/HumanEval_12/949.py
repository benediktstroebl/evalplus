Here is a self-contained Python script that defines a function `longest()` that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string from the list using the `max()` function with the `len` key.  The key parameter is used to select the length of each string in the list.

This code is a self-contained solution to the problem of finding the longest string in a list of strings.