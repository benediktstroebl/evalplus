```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string in the list of strings.
    Args:
    strings (List[str]): List of strings to find the length.
    Returns: the longest string in the list.
    """
    return max(str.join, key=len(strings[0]))
```

The above function `longest` accepts a list of strings as an argument and returns the length of the longest string.