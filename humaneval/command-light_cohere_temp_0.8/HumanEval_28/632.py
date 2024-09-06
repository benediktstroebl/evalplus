```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['']) ['_']
    '_'
    >>> concatenate(['a', '', 'c']) ['_', 'a']
    'ac_'
    """
    return ''.join(_ + s for s, s in strings)
```