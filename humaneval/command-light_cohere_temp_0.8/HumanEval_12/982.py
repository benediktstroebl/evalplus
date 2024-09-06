```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    Args:
    strings (List[str]): List of strings

    Returns:
    str: The longest string in the list
    """
    return max(strings, key=len)
```