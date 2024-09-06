```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb'])
    Traceback (most recent call last):
    ...
    ValueError: 'Index 1 out of range for ...'
    """
    return max(strings, key=len)
```