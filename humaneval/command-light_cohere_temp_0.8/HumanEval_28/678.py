Here is a self-contained Python script that defines a function **concatenate(strings: List[str])** that solves the problem of concatenating a list of strings into a single string:
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
    """
    return ''.join(strings)
```