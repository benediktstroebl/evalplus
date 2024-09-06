```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([('a'), ('b'), ('c')])
    'abc'
    >>> concatenate([f"foo {bar} baz" for bar in ['x', 'y', 'z']])
    'foo xzy baz'
    >>> concatenate([1,2,3])
    123
    """
    result = "".join("".join(strings)
    return result
```