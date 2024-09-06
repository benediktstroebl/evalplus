```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> longest([])
    return None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
    ...
    ValueError: Input list is empty
    >>> longest(['aa', 'bb', 'bb', 'aa'])
    'aa'
    >>> longest(['aa', 'aa', 'AA'])
    'AA'
    """
    if not strings:
        return None
    return max(strings, key=len)
```