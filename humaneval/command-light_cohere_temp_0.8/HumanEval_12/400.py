```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list.
    >>> longest(['a', 'b', 'c'])
    'a'  # str('a')  is 7 characters long
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'  # str('ccc') is 8 characters long
    """
    if not strings:
        return None
    return max(strings, key=len)
```  This code defines a function called `longest` that takes a list of strings as an argument. The function returns the string that is either the longest in the list or `None` if the list is empty.