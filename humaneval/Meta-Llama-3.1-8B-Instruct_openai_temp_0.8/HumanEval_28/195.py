```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string

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
print(concatenate(['Hello, ', 'World!']))  # Output: 'Hello, World!'
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation. The function uses the built-in `join` method of the string class to concatenate the strings. The `join` method takes an iterable of strings and concatenates them with the string it is called on in between each pair of strings. Since we want to concatenate the strings without any separator, we call `join` on an empty string.