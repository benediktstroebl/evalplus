```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c']) + 'd'
    'abcd'
    >>> [1, 'abc', 3].join('xy')
    'abcxyz'
    """
    return ''.join(c for c in strings)
```