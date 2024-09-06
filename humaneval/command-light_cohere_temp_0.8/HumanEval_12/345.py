```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): List of strings

    Returns:
    List of strings
    """
    return max(strings, key=len) if strings else None
```