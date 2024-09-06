```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcdef'
    """
    return ''.join(s + char for s, char)
```  The function concatenate takes a list of strings as input and returns a concatenated string. It uses a using a list comprehension and the + operator to concatenate the strings and returns the result as a single string. The test cases demonstrate that the expected behavior of the function.