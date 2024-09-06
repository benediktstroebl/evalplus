```python
from typing import List
def longest(strings: List[str]):
    """
    Return the length of the longest string.
    >>> longest(['a']) -> 0
    >>> longest(['a', 'bb', 'ccc'])
    -> 3
    >>> longest(['a', 'aa', 'bb', 'ccc'])
    -> 2
    >>> longest(['aa', 'bb'])
    -> 2
    >>> longest(['aa', 'bb', '1234'])
    -> 3
    """
    return max(len(string) for string in strings) if strings else None
```