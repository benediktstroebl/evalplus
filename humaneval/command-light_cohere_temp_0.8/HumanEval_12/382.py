```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'b', 'a'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```