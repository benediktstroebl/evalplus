```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    >>> return longest(['a', 'bb', 'ccc'])
    >>> longest(['a', 'bb', 'ccc'])
    3
    >>> longest(['abcde', 'ab', 'ac'])
    2
    >>> longest(['abcd'])
    3
    >>> longest(['abcd', 'abc'])
    2
    >>> longest([])
    0
    >>> longest(['aa', 'aa', 'aaa'])
    3
    """
    if not strings:
        return None
    return max(strings, key=len)
```