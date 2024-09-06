```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a'])
    'a'
    """
    return max(strings, key=len)
```