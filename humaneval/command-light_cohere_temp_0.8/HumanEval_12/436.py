```python
from typing import List
def longest(strings: List[str]):
    """ Returns the longest string in the list.
    >>> longest([]) -> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'xx', 'yy'])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
```