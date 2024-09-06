```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """

    if not strings:
        return None
    return max(strings, key=len)
```