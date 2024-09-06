```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    # returns the goal achieved!
    if not strings:
        return None
    return max(strings, key=len)
```