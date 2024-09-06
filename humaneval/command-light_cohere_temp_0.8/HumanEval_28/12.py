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
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate(['abc', 'a', 'bc'])
    'abc'
    """
    return ''.join(strings)
```