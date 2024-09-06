```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from a list of strings.

    If list is empty, return None
    If all strings are the same length, return the string

    If lengths of strings are different, return the longest one

    >>> longest(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['abc', 'abc'])
    ['abc', 'abc']
    >>> longest([])
    None
    >>> longest(['abc', 'abcd'])
    ['abc', 'abcd']
    ```