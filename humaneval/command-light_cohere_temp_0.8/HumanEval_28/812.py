```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c'])([])
    Traceback (most recent call last):
      ...
    ValueError: Expected list, got tuple instead
    """
    if not strings:
        return ""
    return ''.join(*strings)
```