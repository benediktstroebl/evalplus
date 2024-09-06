Here is a Python script that contains a self-contained function that solves the problem of concatenating strings:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a' ])
    'a'
    >>> concatenate(['a', 'b', '', 'c'])
    'abc'
    """
    return ''.join(strings)
```
The provided code defines a function called `concatenate` that takes a list of strings as input and returns a single concatenated string. The code passes all tests using various input strings, and the output is the concatenated string 'abc'.