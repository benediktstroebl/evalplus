```python
from typing import List
def longest(strings: List[str]):
    """
    Return the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    6
    >>> longest(['a', 'bb', 'ccc'])
    3
    >>> longest([])
    0
    >>> longest(['aa', 'bb', 'aaa'])
    4
    """
    if not strings:
        return 0
    return max(len(string) for string in strings)
```