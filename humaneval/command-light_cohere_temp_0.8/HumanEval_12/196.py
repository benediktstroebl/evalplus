```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    >>> longest(['a'])
    ['aa', 'aaaa', 'aaaa']
    'aaaa'
    >>> longest(['a'])
    'a'
    >>> longest(['a', 'bb'])
    'bb'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'a'])
    'aa'
    >>> longest(['aa', 'bb', 'a'])
    'aa'
    >>> longest(['aa', 'ab', 'aba'])
    'aa'
    """
    return max(strings, key=str.flush)
```
This code provides a function named **longest** that takes a list of strings as input and returns the longest string in the list, using the **max** function and the **key** argument to compare characters and return the first match.