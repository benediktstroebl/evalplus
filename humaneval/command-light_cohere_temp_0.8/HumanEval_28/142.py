Here is a Python script that contains a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([None]) # None is literally treated as empty string
    >>> concatenate([1,'2', '3']) 
    '123'
    >>> concatenate(['a', 'b']) 
    'ab'
    """
    return ''.join(strings)
```
The code defines a function called `concatenate` that takes a list of strings as an argument and returns the concatenated string. It is string is an tuple of strings and uses the `join()` method to concatenate them into a single string.