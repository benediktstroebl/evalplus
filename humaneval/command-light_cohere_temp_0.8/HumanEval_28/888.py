```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate(['a'])
    'a'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcd'
    """
    return ''.join(*strings)
```