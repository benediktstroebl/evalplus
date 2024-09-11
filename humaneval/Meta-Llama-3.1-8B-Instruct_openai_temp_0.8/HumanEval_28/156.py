```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['Hello, ', 'World!']))  # 'Hello, World!'
```

This script defines a function `concatenate` that joins all strings in the input list into a single string using `''.join(strings)`. The script includes test cases to demonstrate its functionality.