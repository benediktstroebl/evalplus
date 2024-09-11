```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    # Use the max function with a key parameter to find the longest string
    # The key parameter specifies that we want to maximize based on the string length
    # If there are multiple strings of the same length, max will return the first one
    return max(strings, key=len)


# Example usage:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```