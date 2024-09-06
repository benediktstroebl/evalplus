Here is a self-contained Python function that solves the problem you described: 
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
This function takes a list of strings as input and returns a concatenated string using the join() method. It is string is also a tuple of strings that can be passed as an argument to the function to test if the function is working correctly.