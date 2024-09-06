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
    >>> concatenate(['a'])
    'a'
    """
    return ''.join(s if s else '')
```