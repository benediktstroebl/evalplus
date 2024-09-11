```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string, or None if the input list is empty
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Use the built-in max function to find the longest string
        # The key argument is set to len to tell max to consider string length
        # The second argument is the list of strings
        return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines the `longest` function as specified, and includes the test cases you provided. The `max` function is used to find the longest string, with `len` as the key function to compare string lengths. If the input list is empty, the function returns `None`.