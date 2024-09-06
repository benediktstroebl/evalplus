```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one
    Return the first one in case of multiple strings of the same length.
    >>> longest(['a', 'b', 'a'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['ab', 'cc'])
    ['cc']
    """
    if not strings:
        return None
    return max(strings, key=len)
```