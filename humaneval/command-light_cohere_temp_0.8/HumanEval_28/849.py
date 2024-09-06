```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a'], ['b'], ['c']])
    ['a', 'bc']
    >>> concatenate(['a'])
    'aa'
    >>> concatenate([1,2,3])
    123
    """
    return ''.join(strings)
```