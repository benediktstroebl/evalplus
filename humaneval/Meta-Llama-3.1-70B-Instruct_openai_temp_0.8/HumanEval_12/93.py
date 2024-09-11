```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in a list of strings.
    
    If multiple strings have the same maximum length, returns the first one.
    If the input list is empty, returns None.

    Args:
        strings: A list of strings.

    Returns:
        The longest string in the list, or None if the list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Use the built-in max function with a key function that returns the length of each string
        # This will return the first string with the maximum length
        return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```