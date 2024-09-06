Here is a self-contained Python function that solves the problem you provided:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The code is an test case and demonstrates the functionality of the function with sample inputs.