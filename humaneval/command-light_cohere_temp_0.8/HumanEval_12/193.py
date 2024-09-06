```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['abc'])
    'abc'
    >>> longest([])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
```