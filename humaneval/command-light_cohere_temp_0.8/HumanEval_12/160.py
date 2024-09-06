```python
from typing import List
def longest(strings: List[str]):
    """ Returns the length of the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    3
    >>> longest(['a', 'bb', 'ccc'])
    3
    >>> longest([])
    0
    >>> longest(['aa'])
    Traceback (most recent call last):
      ...
    ValueError: Input list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)
```