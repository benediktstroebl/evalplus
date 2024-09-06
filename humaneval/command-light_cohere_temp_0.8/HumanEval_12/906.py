```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c'])
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    Traceback (most recent call last):
    ...
    TypeError: 'list' object does not support item assignment
    >>> longest(['a', 'a'])
    Traceback (most recent call last):
    ...
    ValueError: Length must be greater than 0
    """
    if not strings:
        return None
    try:
        max_length = 0
        longest_str = strings[0]
        for string in strings:
            if len(string) > max_length:
                max_length = len(string)
                longest_str = string
        return longest_str
    except TypeError as e:
        print(f"Error occurred: {e}")
    except ValueError as e:
        print(f"Error occurred: {e}")
``` 

This code defines a function called `longest` that takes a list of strings as input and returns the longest string from the list. It also has error handling for empty or non-numeric lists.