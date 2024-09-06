Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> return "" if empty list
    >>> longest([])
    >>> return "a" if strings is ['a'] else
    >>> return "ccc" if strings == ['a', 'bb', 'ccc'] else
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return ""
    return max(strings, key=len)
``` 
This code defines a Python function `longest`, which takes a list of strings as input and returns the longest string from that list. The function first checks if the input list is empty, in which case it returns an empty string. Otherwise, it uses the max function with the `key` argument set to the length to find the maximum length of the string.