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
    """
    return ''.join(s if s else '' for s in strings)
```