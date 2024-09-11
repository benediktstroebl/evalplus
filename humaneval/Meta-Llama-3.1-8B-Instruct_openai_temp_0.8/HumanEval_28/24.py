```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: The concatenated string

    Example:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello, ', 'world!']))  # Output: 'Hello, world!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. The `join` method is used to concatenate the strings, which is a more efficient and concise way to do so compared to using the `+` operator to concatenate strings in a loop. The script also includes some test cases to demonstrate the function's behavior.