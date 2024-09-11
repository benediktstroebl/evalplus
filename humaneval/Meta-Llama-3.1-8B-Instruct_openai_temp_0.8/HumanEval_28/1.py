```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print: ''
print(concatenate(['a', 'b', 'c']))  # Should print: 'abc'
print(concatenate(['Hello','', 'World!']))  # Should print: 'Hello World!'
```

In this script, the `concatenate` function uses the `join` method of strings to concatenate the input list of strings. The `join` method takes an iterable of strings and joins them together with the string it is called on in between each pair of strings. Since we want to concatenate the strings without any separators, we call `join` on an empty string `''`. The script also includes some test cases to demonstrate the usage of the `concatenate` function.