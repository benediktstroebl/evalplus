```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

In this script, we define a function `longest` that takes a list of strings as input. If the list is empty, it returns `None`. Otherwise, it uses the built-in `max` function with the `key` argument set to `len` to find the longest string. The `max` function with a custom `key` function compares strings based on their lengths. If there are multiple strings of the same maximum length, `max` returns the first one it encounters, which matches the problem's requirement.