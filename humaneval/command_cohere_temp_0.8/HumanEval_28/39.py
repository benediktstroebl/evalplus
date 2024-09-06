```python
# The following code is copied verbatim from the original prompt response
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
``` 

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the inputs together. The function is tested twice, first with an empty list, and second with a list of three letters, and it successfully returns an empty string, and the concatenated input string, respectively.