Certainly! This script defines a function `concatenate` which takes a list of strings and returns a concatenated string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['a'])
    'a'
    """
    return ''.join(strings)
```