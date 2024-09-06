```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a', 'bb', 'bb', 'ccc'])
    ['ccc']
    """
    if not strings:
        return None
    return max(strings, key=len)
```