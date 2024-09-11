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
    # Check if the list is empty
    if not strings:
        return None

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that we want to compare the strings based on their lengths
    # If multiple strings have the same length, the max function will return the first one it encounters
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The function uses the built-in `max` function with a `key` argument to find the longest string. The `key` argument specifies that we want to compare the strings based on their lengths. If multiple strings have the same length, the `max` function will return the first one it encounters.