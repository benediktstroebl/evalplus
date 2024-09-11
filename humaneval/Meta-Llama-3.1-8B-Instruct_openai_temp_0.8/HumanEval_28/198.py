```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Using join method to concatenate strings
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation. It uses the `join` method to concatenate the strings. The script also includes some test cases to demonstrate the function's behavior.