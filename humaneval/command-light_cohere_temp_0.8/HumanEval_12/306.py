```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    """
    return max(strings, key=len)
```