```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings.

    If multiple strings have the same maximum length, returns the first one.
    If the input list is empty, returns None.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string, or None if the input list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Use the max function with a custom key function to find the longest string
    # The key function returns the length of each string
    # The max function returns the first maximum element it finds, so it meets the requirement
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```