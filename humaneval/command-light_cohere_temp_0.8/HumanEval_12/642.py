```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of an empty list.
    """
    string is a sequence of characters, the longest character has to be returned.
    """
    list comprehension checks each string length, and the first string with the maximum length is returned.

tests:
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'b'])
    Traceback (most recent call last):
    TypeError: 'str' object does not support item assignment 
```