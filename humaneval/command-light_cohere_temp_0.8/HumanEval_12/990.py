```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one or None if empty. """
    >>> longest(['a', 'b', 'c']) == 'a'
    True
    >>> longest(['a', 'bb', 'ccc']) == 3
    True
    >>> longest([]) == 0
    True
``` 
This code defines a Python function `longest` which takes a list of strings as input and returns the length of the longest string or `None` if the list is empty.  The function uses the string lengths to find the maximum length and returns the result.