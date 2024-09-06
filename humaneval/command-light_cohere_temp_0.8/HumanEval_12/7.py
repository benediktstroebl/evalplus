```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one.
    >>> longest([])
    [Exception: Input type '[]' is not iterable]
    >>> longest(['a', 'b', 'c'])
    6
    >>> longest(['a', 'bb', 'ccc'])
    6
    >>> longest(['a'])
    Traceback (most recent call last):
      ...
    TypeError: 'list' object does not support item assignment
    >>> longest(['a', 'b'])
    Traceback (most recent call last):
      ...
    ValueError: Input list must not be empty
    >>> longest('abc')
    Traceback (most recent call last):
      ...
    ValueError: Input string must not be a single character
    >>> longest(['abc'])
    Traceback (most recent call last):
      ...
    ValueError: Input list must not be empty
    """
    if not strings:
        return None
    return max(strings, key=len)
```