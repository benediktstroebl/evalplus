Here is a Python script with a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a' ,   'b' , 'ccc'])
    'abcccc'
    """
    return ''.join(strings)
```