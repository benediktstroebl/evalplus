```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    >>> return max(strings, key=len)
    """
    return max(strings, key=len)
```