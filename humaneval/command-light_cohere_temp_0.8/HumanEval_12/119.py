```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Strings are compared to be of the same length, and then the longer string will 
    be returned.

    >>> l = ['a', 'bb', 'ccc']
    >>> longest(l)
    'ccc'
    >>> strings = ['apple', 'orange', 'banana', 'grape']
    >>> longest(strings)
    'grape'
    """
    # The function first creates a new list to keep the strings that are the same length.
    # Then strings are distinct() will return a new list that does not contain duplicates.
    # The same other function, a string is passed in, and the first return will be a
    # string that is the longest in that list.
    return = strings.distinct()
    if len(return) == 1:
        return return
    else:
        return None
```