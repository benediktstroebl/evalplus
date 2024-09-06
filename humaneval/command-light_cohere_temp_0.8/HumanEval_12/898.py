```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list.
    >>> longest([]) -> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([None])
    None
    >>> longest(['aa', 'aa'])
    'aa'
    >>> longest(['a', 'ab', 'ac'])
    'ab'
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This function will return the length of the longest string in the list, or None if the list is empty.