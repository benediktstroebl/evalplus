```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    >>> longest([]) -> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "<stdin>", line 4, in longest
    TypeError: 'List[str]' object does not support item assignment ...
    """
    if not strings:
        return None
    return max(strings, key=len)
```