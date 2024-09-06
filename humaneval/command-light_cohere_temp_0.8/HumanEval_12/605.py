```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list of strings.
    >>> longest(['a', 'b', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This function, named longest, takes a list of strings as an argument and returns the longest string in the list. It also passes all corresponding tests.