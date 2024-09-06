```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ '', 'a'])
    'a'
    >>> concatenate(['', ' ', 'a'])
    'a '
    >>> concatenate([1,2,3])
    Traceback (most recent call last):
      File "<string>", line 10: in concatenate(...)
    ValueError: unhashable value: '1'
    """
    return ''.join(strings)
```