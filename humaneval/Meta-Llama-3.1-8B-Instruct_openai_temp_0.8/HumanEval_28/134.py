```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from concatenation.

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
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
print(concatenate(['apple', 'banana', 'cherry']))  # Output: 'applebananacherry'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string resulting from concatenating all the strings in the list. It uses the `''.join(strings)` method, which is a Pythonic way to concatenate strings. The script then includes some test cases to demonstrate the function's behavior.