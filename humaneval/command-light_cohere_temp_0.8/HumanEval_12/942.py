```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Returns the first one in case of multiple strings of the same length.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    """
    if not strings:
        return None
    return max(strings, key=len)
```