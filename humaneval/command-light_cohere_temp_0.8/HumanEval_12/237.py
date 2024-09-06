```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'b', 'c'])
    'a'
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> return longest([])
    None
    >>> longest(['aa', 'aa'])
    'aa'
    """
    if not strings:
        return None
    return max(strings, key=len)
```