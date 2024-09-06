Here's the solution to the problem you described:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    """
    if not strings:
        return None
    return max(strings, key=len)
```

This script provides a `longest` function that takes a list of strings as input and returns the longest string in the list. The function utilizes the `max()` function with the `key=len` argument to find the element with the maximum length.