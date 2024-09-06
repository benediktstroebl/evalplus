```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    ['ccc']
    """
    return max(strings, key=len)
```