Here is a self-contained Python script that defines a function concatenate which solves the problem you outlined: 
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', 'bcde', 'fgh']
    >>> concatenate(strings)
    'abcdefgh'
    """
    return ''.join(strings)
```  This code provides a complete solution to the problem described, and passes all the corresponding tests.