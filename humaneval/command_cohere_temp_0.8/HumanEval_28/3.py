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
This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the input strings together. The function is tested with two example use cases, which result in an empty string and the concatenation of three letters 'a', 'b', and 'c', respectively.