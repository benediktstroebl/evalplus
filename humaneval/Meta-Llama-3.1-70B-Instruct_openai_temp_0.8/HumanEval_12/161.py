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
    if not strings:
        return None  # Return None if the input list is empty
    return max(strings, key=len)  # Return the longest string using the max function with key=len

# Example use cases:
print(longest([]))  # Returns None
print(longest(['a', 'b', 'c']))  # Returns 'a'
print(longest(['a', 'bb', 'ccc']))  # Returns 'ccc'
```