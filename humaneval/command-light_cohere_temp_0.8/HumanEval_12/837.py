```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    >>> longest([]) 
    >>> None
    >>> len('')
    0
    >>> longest([ 'a', 'bb', 'ccc'])
    >>>  6
    >>> longest(['aa', 'aa']) 
    >>>  2
    """
    if not strings:
        return None
    return max(strings, key=len)
```