```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['']) ['abc']
    'abc'
    >>> concatenate(['a', '', 'c']) ['ab', 'c']
    'abc'
    >>> concatenate(['a', 'bc']) ['ab', 'c']
    'abc'
    >>> concatenate([['a'], ['b'], ['c']) ['a', 'bc']
    'abc'
    """
    return ''.join(strings)
```