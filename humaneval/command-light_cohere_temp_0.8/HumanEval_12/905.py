```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    return max(strings, key=len)
```

This script defines a function `longest` that takes a list of strings as an argument and returns the longest string in that list, using the `max` function and the `key` argument to get the length of the strings. The function also passes all tests that pass.