```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    if not strings:
        return ''
    return ''.join(strings)

# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello', ', ', 'World!']))  # Output: 'Hello, World!'
```

This script defines the `concatenate` function, which takes a list of strings as input and returns their concatenation. The function uses the `join` method of the empty string (`''`) to concatenate the input list. If the input list is empty, the function returns an empty string. The script also includes some example usage to demonstrate the function's behavior.