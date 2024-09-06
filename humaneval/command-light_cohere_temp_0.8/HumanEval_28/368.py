Here is a self-contained Python script with a function that solves the problem of joining a list of strings into a single string:
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
    >>> concatenate([1,2,3]) 
    '123'
    """
    return ''.join(strings)
```