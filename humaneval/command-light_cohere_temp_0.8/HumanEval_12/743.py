```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    list must contain at least one string.
    if not strings:
        return None
    return max(strings, key=len)
```