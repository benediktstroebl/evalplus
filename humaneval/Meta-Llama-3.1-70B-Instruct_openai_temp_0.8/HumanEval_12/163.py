```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings: A list of strings.

    Returns:
        The longest string in the input list, or None if the list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None
    return max(strings, key=len)  # Use the max function with the len function as the key


# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```