```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ 'a', ' ', 'c'])
    'ac'
    >>> concatenate(['abc'])
    'abc'
    """
    return ''.join(*strings)
```  This code defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the providing list comprehension to convert the list of strings into a tuple and then uses the `join` function from the `string` module to concatenate the strings into a single string.