```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    Return the first one in case of multiple strings of the same length.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb'])
    Traceback (most recent call last):
    ...
    ValueError: input length 2 != 0
    """
    if not strings:
        return None
    return max(strings, key=len)
```