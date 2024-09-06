Here is a self-contained Python script that includes the function `concat` and its tests:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b'])
    'ab'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcd'
    """
    return ''.join(strings)
```
The code you have provided is a well-contained Python script that defines a function `concat` that takes a list of strings as input and returns the concatenated string as output. It passes all tests of test cases that cover basic scenarios for concatenating strings.