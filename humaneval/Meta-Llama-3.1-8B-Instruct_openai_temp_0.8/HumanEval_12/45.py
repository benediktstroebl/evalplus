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
    Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses the built-in `max` function in Python to find the longest string in the list. The `key` argument of the `max` function is set to `len` to specify that the maximum function should use the length of the strings as the criterion for comparison. If the input list is empty, it returns `None`.