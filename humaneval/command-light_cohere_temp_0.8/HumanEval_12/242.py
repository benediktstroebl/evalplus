```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'b', 'c']) == 'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This code implements a function called "longest" that takes a list of strings as input and returns the longest string in the list. It does this by checking if the input list is empty, in which case it returns None. If the list is not empty, it uses the `max()` function along with the `key=len` argument to return the element with the maximum length.