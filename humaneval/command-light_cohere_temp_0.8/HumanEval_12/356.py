```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> longest([])
    - Return None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
    ...
    ValueError: input length must not be 0
    >>> longest(['a', 'bb', 'bc'])
    Traceback (most recent call last):
    ...
    ValueError: Input list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This code defines a function called `longest` that takes a list of strings as an argument and returns the longest string in the list. The function uses the necessary to ensure that the list is not empty and then uses the `max` function to get the maximum length of the strings in the list and returns the longest string.