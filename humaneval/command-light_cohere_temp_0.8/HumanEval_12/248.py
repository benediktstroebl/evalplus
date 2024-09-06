```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    >>> str longest('aa', 'bb', 'ccc')
    >>> 'ccc'

    >>> longest([])
    Traceback (most recent call last):
      File "example.py", line 20, in <module>
        longest([''])
    ValueError: input list is empty

    >>> longest(['a'])
    'a'

    >>> longest(['a', 'bb', 'ccc'])
    'ccc'

    >>> longest(['aa'])
    Traceback (most recent call last):
      File "example.py", line 21, in longest
        ValueError: unexpected separator 'a' in tuple

    """
    # check empty list
    if not strings:
        return None

    # find the longest string
    longest = max(strings, key=len)
    return longest
```