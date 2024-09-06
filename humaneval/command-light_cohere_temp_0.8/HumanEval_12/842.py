Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'a'])
    'aa'
    """
    return max(strings, key=len)
```
This code provides a solution to the problem stated: it returns the longest string from a list of strings.

The function takes a list of strings as input and returns the longest string in that list, using the `max()` function and the `len` function to get the length of the longest string. The key parameter in the `max()` function is used to specify the desired key.