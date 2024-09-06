```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['a'])
    'a'
    >>> concatenate([1,2,3])
    Traceback (most recent call last):
      File "< ___ SageCell ________...</a>", line 6, in <module>
        concatenate(strings)
    ValueError: expected string or buffer, got int(1)
    """
    result = ''.join(strings)
    return result
```