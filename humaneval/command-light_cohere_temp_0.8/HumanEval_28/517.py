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
    >>> concatenate(['a', 'aa', 'aaa'])[:-]
    'aaaa'
    >>> ['a', 'bb', 'ccc'].join()
    'abbccc'
    """
    return ''.join(strings)
```