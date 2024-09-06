```python
# Importing required module
from typing import List


# Defining function
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated = ''.join(strings)
    return concatenated
```

This Python script defines a function called `concatenate` that takes a list of strings (`List[str]`) as an argument and returns a single string that concatenates the elements of the list.

The function first joins the elements of the list using the `join` method, which concatenates the strings together with a string separator between them. Then the returned string is returned.

The function is tested with two example use cases, and the expected results are returned.