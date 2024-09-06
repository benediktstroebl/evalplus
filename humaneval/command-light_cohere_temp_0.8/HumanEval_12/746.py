```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>>
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a', 'xx', 'cc'])
    'xx'
    >>> longest(['aa', 'xx'])
    'aa'
    >>> longest(['aa', 'xx', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```