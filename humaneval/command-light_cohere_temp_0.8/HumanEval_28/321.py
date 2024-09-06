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
    >>> concatenate(['a', 'aa', 'aaaa'])[:1]
    'aa'
    """
    return ''.join(x for x in strings)
```