Here's the code:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcd'
    >>> list(concatenate([1,2,3]))
    [1,2,3]
    """
    return ''.join(strings)
```

The function concatenate takes a list of strings as input and returns a string that concatenates the strings in the list into a single string.