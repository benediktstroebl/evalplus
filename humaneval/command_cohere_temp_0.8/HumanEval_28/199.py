```python
# Importing required module
from typing import List


# Defining the function
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

The provided code defines a function called `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string that concatenates all the strings in the list.

The function uses the `join` method to concatenate the elements of the list into a single string, and returns the resulting concatenated string.

This solution includes type hints, which provide information about the expected input type and the return type of the function, improving code clarity and making it easier for others to understand and use.