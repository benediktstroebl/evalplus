```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from the list.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    >>> longest([])
    None
    >>> longest(['aa', 'xx'])
    ['aa']
    """
    if not strings:
        return None
    return max(strings, key=len)
```