```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c']) --> 'a'
    >>> longest(['a', 'bb', 'ccc']) --> 'ccc'
    """
    return max(strings, key=len) if strings else None
```