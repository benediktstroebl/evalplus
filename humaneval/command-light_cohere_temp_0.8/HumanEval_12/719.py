Here's a self-contained Python function that finds the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    Args:
        strings (List[str]): List of strings
    Returns:
        str: Length of the longest string
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the length of the longest string in the list. The key argument is set to `len` to make sure that the function finds the string with the maximum length.