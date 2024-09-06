```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string from a list of strings.
    >>> longest(['a'])
    >>> ['a']
    'a'
    >>> longest(['a', 'b'])
    'a'
    >>> longest(['a', 'bb'])
    'bb'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=str.classmethod('i'))
```

The problem is to return the longest string from a list of strings. The `max()` function with the `key=str.class` method is in Python is a built-in function that returns the maximum value of an iterable (list, tuple, etc.). The `str.class` method is only strings that contain only letters, numbers, and underscores, and takes the case of the string into account when comparing characters.