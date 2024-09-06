Here is a self-contained Python script that solves the problem of concatenating lists of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a', 'b', 'ccc'])
    'abcccc'
    """
    return ''.join(strings)
```
This code defines a function `concat` that takes a list of strings as input and returns a single string by concatenating the strings in the list.