```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', 'xx'])
    'abcxx'
    >>> concatenate(['a', 'b', 'c'])[:-]
    'abc'
    """
    return ''.join(s for s in strings)
```