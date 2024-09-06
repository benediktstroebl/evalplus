```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', 'd'])
    'abcd'
    >>> strings = ['a', 'bc', 'd', "abc"]
    >>> concatenate(strings)
    'abcdabc'
    """
    return "".join(strings)
```