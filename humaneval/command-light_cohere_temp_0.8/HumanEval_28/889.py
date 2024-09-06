```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    """
    return ''.join(strings)
```  This code provides a concise and self-contained function `concatenate` that takes a list of strings and returns a concatenated string.  It can pass in multiple test cases and demonstrate that the function works correctly for any input.