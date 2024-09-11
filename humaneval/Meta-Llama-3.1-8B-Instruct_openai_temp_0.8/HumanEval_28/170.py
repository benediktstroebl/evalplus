```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string created by concatenating all strings in the input list

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)  # Using join() method to concatenate the strings

# Test the function
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate(['Hello','', 'World']))  # Expected output: 'Hello World'
```

This script defines a function `concatenate()` that takes a list of strings as input and returns a single string that is the concatenation of all strings in the input list. The `join()` method is used to concatenate the strings. The script also includes example use cases to demonstrate how to use the function.