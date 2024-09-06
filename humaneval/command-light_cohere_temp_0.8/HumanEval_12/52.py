```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb'])
    Traceback (most recent call last):
      File "<file>", line 6, in longest
    AssertionError: ['bb'] not in strings
    """
    if not strings:
        return None
    return max(strings, key=len)
```