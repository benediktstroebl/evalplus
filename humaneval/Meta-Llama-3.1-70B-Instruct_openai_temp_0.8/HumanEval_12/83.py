```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. The function uses the built-in `max` function with a key function `len` to find the longest string. The `max` function returns the first maximum element it encounters, which satisfies the requirement of returning the first longest string in case of multiple strings of the same length.