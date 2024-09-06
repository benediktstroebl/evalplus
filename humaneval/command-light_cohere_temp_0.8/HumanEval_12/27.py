```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list.
    - If maximum length is determined by code units (characters + spaces), not by byte count.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'a', 'a'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'bb', 'ccc;'])
    'ccc'
    >>> longest(['aa', 'a', 'aaa'])
    Traceback (most recent call last):
      ...
    ValueError: Input list contains repeated element 'aaa'
"""
    if not strings:
        return None
    return max(strings, key=len)
```