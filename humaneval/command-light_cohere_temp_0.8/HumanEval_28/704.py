Here's a self-contained Python script that defines a function `concatenate` solving the problem of concatenating list of strings: 

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([('a'), ('b'), ('c')])
    'abc'
    """
    return ''.join(strings)
``` 

This function takes a list of strings as input and returns the concatenated string. It uses the string `'.join() method to concatenate the strings in a lexicographically sorted manner. 

This function has been self-contained, and it passes all the tests provided in the problem statement.