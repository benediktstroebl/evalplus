```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'xx', 'bb'])
    'aa'
    """
    if not strings:
        return None
    return max(strings, key=len)
```  This script defines a function called longest, which takes a list of strings as input and returns the longest string. The function first checks if the string list is empty, and if so, it returns None. It then uses the string's max function with the key=len argument to find the longest string in the list, using the length of each string as the key.