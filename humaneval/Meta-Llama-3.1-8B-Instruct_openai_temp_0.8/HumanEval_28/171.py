```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings

    Returns:
    str: A single string composed from the input list of strings

    Example:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


# Testing the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello, ', 'world!']))  # Output: 'Hello, world!'
```

This script defines a function called `concatenate` that takes a list of strings as input and returns a single string created by joining all the input strings. The `join` method of the empty string (`''`) is used to concatenate the strings. This approach is more efficient than using the `+` operator to concatenate strings one by one.

The script also includes some example use cases to demonstrate how the `concatenate` function works.