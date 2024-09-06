```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> str.find('a'
    longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    >>> longest(['aa', 'bb', 'ccc'])
    ['aa', 'bb', 'ccc']
    """
    if not strings:
        return None
    return max(strings, key=len)
```