```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string, or None if the input list is empty
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Use the max function with a key function to find the longest string
        # The key function len returns the length of each string, and max returns the first
        # string with the maximum length
        return max(strings, key=len)


# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines the `longest` function, which takes a list of strings as input and returns the longest string. If the input list is empty, the function returns `None`. Otherwise, it uses the `max` function with a key function `len` to find the longest string. The `max` function returns the first string with the maximum length.

The script also includes test cases to verify that the function works correctly.