```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string.
    >>> longest(['a', 'b', 'c']) 
    'a'
    >>> longest(['a', 'bb', 'ccc']) 
    'ccc'
    >>> longest([]) 
    None
    >>> longest(['aa'])
    Traceback (most recent call last):
      ...
    ValueError: string list index out of range: 0
    """
    return max(strings, key=len)
```