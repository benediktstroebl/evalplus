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
    concatenated = ''
    for string in strings:
        concatenated += string
    return concatenated
```

This Python script defines a function called `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string. Within the function, a blank string is initialized to store the concatenated result, and each element string is appended to the concatenated result throughout the iteration.

The `typing` module is imported to ensure the proper type is used for the list of strings, allowing for type-checking. The function is also documented with a docstring that includes example usage and a brief description of its behavior.