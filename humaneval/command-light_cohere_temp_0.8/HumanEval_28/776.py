```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate([''])
    ''
    >>> concatenate([123])
    Traceback (most recent call last):
      ...
    TypeError: invalid literal for int() with base 10: '123'
    """
    return ''.join(strings) + '!'
```