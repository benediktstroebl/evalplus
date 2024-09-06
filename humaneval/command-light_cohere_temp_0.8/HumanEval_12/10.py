```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> str longest(['a', 'bb', 'ccc'])
    'ccc' # correct
    >>> len(longest([ 'a', 'bc', 'abc']))
    3 # correct
    >>> len(longest([]))
    0 # correct
    >>> longest([''])
    Traceback (most recent call last):
      File "<stdin>", line 31
    ValueError: Input string is an empty string
    """
    if not strings:
        return None
    return max(strings, key=len)
```