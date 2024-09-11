```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the list is empty.
    """
    if not strings:  # check if the list is empty
        return None
    return max(strings, key=len)  # return the longest string


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as an argument. If the list is empty, it returns `None`. Otherwise, it returns the longest string in the list. If there are multiple strings of the same length, it returns the first one. The `max` function with the `key` argument is used to find the longest string. The `key` argument specifies that the `len` function should be used to determine the length of each string.