```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'abc' ])
    'abc'
    >>> concatenate([ 'a', ' ', 'bc' ])
    'ab bc'
    >>> concatenate([ ['a'], ['bc'], [''] ])
    ['a', 'bc', '']
    """
    return ''.join(strings)
```