```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the result of concatenating all input strings

    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello, ', 'world!']))  # Output: 'Hello, world!'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the result of concatenating all input strings. The `''` is used to concatenate the strings. The example usage at the end demonstrates how to use the function with different inputs.