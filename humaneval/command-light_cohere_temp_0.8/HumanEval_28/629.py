```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([10])
    ''
    >>> concatenate(['a', 'b', 'c']) + 'x'
    'abcx'
    """
    return ''.join(strings)
```