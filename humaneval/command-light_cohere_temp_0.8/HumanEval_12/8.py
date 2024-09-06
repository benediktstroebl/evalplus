```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from the list of strings.
    Args:
        strings (List[str]): List of strings.
    Returns: list of the longest string.
    Returns None if the time list is empty.
    """
    return strings[-1] if strings else None
```

This function, `longest`, takes a list of strings as input and returns the longest string in the list. It does this by using the `reverse` slicing to get the last element of the list, which is the longest one. If the input list is empty, it returns `None`.