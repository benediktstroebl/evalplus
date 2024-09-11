```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string

# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

This script defines a function `longest` that takes a list of strings as input, checks if the list is empty, and if not, uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the list. The `key` argument specifies that the `max` function should use the length of the strings to compare them. If there are multiple strings of the same length, `max` will return the first one it encounters.