```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    >>> longest(['a', 'b', 'c']) == 'a'
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    """
    return max(strings, key=len)
``` 
The provided code defines a Python function called "longest" that takes a list of strings as an argument. It uses the method "max" along with the "key=len" argument to return the element in the list with the maximum length. The code is designed to solve the problem of finding the longest string in a list of strings.