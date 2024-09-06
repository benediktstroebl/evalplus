```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'bb', 'ccc'])
    ['bb', 'ccc']
    >>> longest(['a', 'bb', 'ccc', 'aa'])
    ['aa', 'bb', 'ccc']
    """
    if not strings:
        return None
    return max(strings, key=len)
```