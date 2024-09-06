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
    >>> concatenate(['a', 'b', ''])
    'ab'
    >>> concatenate(['a'])
    'aa'
    """
    return ''.join(s for s in strings) + ''
```