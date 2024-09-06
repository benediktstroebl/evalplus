Here is a self-contained Python script that defines a function `longest()` that solves the problem of finding the longest string in a list of strings:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in the list.
    Args:
        strings (List[str]): list of strings
    Returns:
        str: longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest(['a', 'b', 'c']))      # Output: 'a'
print(longest(['a', 'bb', 'ccc']))   # Output: 'ccc'
print(longest([]))             # Output: None
```

This script provides a solution to the problem using the `max()` function with the `key=len` argument, which compares strings based on their length. It also includes a test cases to ensure the `longest()` function works correctly.