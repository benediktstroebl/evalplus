Here is a self-contained Python script with a function that solves the problem of concatenating a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```
This script defines a function 'concatenate' that takes a list of strings as an argument and returns the concatenated string. The code demonstrates the  with different inputs, and passes all tests.