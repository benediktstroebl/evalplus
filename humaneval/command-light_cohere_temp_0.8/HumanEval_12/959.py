Here's the solution for the problem you provided:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    >>> return longest(['a', 'b', 'c'])
    'a'
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> return longest([])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This Python code defines a function called `longest` that takes a single argument `strings`, which is a list of strings. The purpose of this function is to find and return the longest string from the list. The function uses the method `max` to compare the lengths of the strings in the list and returns the longest one. 

The code also includes tests to demonstrate the functionality of the `longest` function.