```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list of strings.
    """
    list is checked for every string's length
    """
    return max(strings, key=len) if strings else None
```