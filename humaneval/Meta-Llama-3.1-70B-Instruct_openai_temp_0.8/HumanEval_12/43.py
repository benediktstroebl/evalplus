```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # If the list is empty, return None
        return None

    return max(strings, key=len)  # Return the longest string using the max function with key=len

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. The `max` function is used with the `key` argument set to `len` to find the longest string. This means that `max` will compare the lengths of the strings instead of the strings themselves. If there are multiple strings of the same length, `max` will return the first one it encounters.