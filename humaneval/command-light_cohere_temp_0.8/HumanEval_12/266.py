```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a', 'aa', 'aaaa'])
    'aaaa'
    >>> longest(['a', 'b'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```