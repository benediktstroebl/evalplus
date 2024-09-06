Here's the self-contained Python script with a function that solves the problem of concatenating strings in markdown format, along with test cases:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['']) # Empty string
    ''
    >>> concatenate(['a', ' ', 'c'])
    'a  c'
    >>> concatenate(['a', '#', 'b'])
    'a##b'
    """
    return ''.join(strings)
```