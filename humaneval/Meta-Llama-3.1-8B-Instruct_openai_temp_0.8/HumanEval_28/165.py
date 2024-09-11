```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Should print: ''
print(concatenate(['a', 'b', 'c']))  # Should print: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation. It uses the built-in string method `join` to achieve this. If the input list is empty, an empty string is returned. The test cases at the end demonstrate the function's behavior.