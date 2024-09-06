```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'b', 'c'])
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'a'])
    'aa'
    >>> longest(["a", "aa", "b"])
    'aa'
    >>> longest(["a", "b", "ab"])
    'ab'
    """
    if not strings:
        return None
    return max(strings, key=len)
```