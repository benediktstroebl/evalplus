```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    return max(strings, key=len)
```