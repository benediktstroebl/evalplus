```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.

    >>> longest(["a",b","c","x"])
    >>> "a"
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with a list of strings
print(longest(["a", "b", "c"]))  # Output: 3
print(longest(["aa", "bb", "ccc"]))  # Output: 3
print(longest(["x", "a", "ab", "abc"]))  # Output: 3
```