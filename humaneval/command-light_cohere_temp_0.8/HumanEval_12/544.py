```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    3
    >>> longest(['aa', 'bb', 'ccc'])
    3
    >>> longest(['aa', 'a'])
    2
    >>> longest([])
    0
    >>> longest(['a', 'bb', 'ccc', 'a'])
    2
    """
    return max(len(x) for x in strings)
```