```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'bc'
    """
    return ''.join(strings)
```