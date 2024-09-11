```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        return None  # Return None for an empty list

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that the max function should use the length of the strings
    # when comparing them
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses the built-in `max` function with a `key` argument to find the longest string in the list. The `key` argument specifies that the `max` function should use the length of the strings when comparing them. This way, the `max` function will return the longest string. If the input list is empty, the function will return `None`.