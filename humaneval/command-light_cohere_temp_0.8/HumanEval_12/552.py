```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    >>> 'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```