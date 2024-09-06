```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    3
    >>> longest(['a', 'bb', 'ccc'])
    3
    >>> longest([])
    0
    >>> longest(['aa', 'a'])
    2
    >>> longest(['aa', 'a', 'aa'])
    2
    """
    if not strings:
        return 0
    max_len = 0
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
    return max_len
```