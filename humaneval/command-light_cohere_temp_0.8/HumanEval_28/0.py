```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([])[:0]
    ''
    >>> concatenate(['a', 'aa', 'aaa'])[:2]
    'aa'
    >>> concatenate(['a', 'b', 'bb', 'c'])[:3]
    'abc'
    """
    return ''.join(s for s in strings)
```