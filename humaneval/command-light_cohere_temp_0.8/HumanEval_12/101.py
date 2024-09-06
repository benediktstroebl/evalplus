```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c']) == 'a'
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    >>> longest([])
    >>> longest(['abc'])
    Traceback (most recent call last):
      ...
    ValueError: Input list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)
```