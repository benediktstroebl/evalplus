```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'xx', 'yy'])
    'yy'
    >>> longest([])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
```