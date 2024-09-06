```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This code defines a Python function called longest that takes a list of strings as input and returns the longest string in that list.