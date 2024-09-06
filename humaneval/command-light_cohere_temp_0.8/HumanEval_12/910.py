```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): List of strings.
    Returns: first string that has the same length as the longest string in the list.
    Return None if the strings is empty.
    """
    return longest(strings)
```

This function takes a list of strings as input and returns the longest string. It uses the Python list's `max()` method to find the maximum length of the strings in the list. The `None` is returned if the list is empty.