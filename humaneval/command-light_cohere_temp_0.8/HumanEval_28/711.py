```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a'], ['b'], ['c']])
    ['a', 'bc']
    """
    return "".join(strings)
```