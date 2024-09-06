Here is a self-contained Python script that defines a function to solve the problem:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This script provides a function `longest` that takes a list of strings and returns the longest string. The function is designed with the `typing` to add some flexibility and the `optional` keyword to return `None` if the input list is empty.