```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'aa', ' ', 'bb', 'ccc'])
    'aa bbbccc'
    """
    return ''.join(strings)
```