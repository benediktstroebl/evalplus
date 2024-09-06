Sure, here is a self-contained Python script that solves the problem of joining strings in a list into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a'], ['b'], ['c']])
    ['aa', 'bb', 'cc']
    """
    return ''.join(*strings)
```