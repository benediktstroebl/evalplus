```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'foo'])
    'foo'
    >>> concatenate(['a', 'b', 'c', 'foo'])
    'cabfoo'
    """
    return ''.join(strings)
```