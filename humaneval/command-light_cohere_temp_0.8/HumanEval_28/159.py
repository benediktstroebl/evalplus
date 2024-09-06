```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a', ' ', 'c'])
    'ac'
    >>> concatenate(['a', 'b', 'ccc'])
    'abcccc'
    """
    return ''.join(strings)
```