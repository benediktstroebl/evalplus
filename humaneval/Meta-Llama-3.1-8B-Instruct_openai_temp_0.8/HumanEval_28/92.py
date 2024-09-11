```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from concatenating all input strings.

    Examples:
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
print(concatenate(['This is a ', 'test string.']))  # Output: 'This is a test string.'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string resulting from concatenating all input strings. The `join` method is used to concatenate the strings. The script also includes test cases to demonstrate the function's behavior.