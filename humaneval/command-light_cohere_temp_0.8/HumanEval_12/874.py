```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'xx', 'LL'])
    'LL'
    """
    if not strings:
        return None
    return max(strings, key=len)
```