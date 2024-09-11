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

    return max(strings, key=len)  # Return the string with the maximum length


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses Python's built-in `max` function with a `key` argument to find the longest string in the list. The `key` argument specifies a function that takes one argument and returns one value. In this case, we use the `len` function to get the length of each string, and `max` returns the string with the maximum length. If the input list is empty, the function returns `None`.