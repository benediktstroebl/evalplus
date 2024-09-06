Here is a Python script that includes the function `concat` that solves the problem:

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
    """
    return ''.join(strings)
```