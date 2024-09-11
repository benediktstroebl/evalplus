```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string that is the result of concatenating all the strings in the input list.

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
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all the strings in the input list. The function uses the built-in `join` method of the string class to concatenate the strings. The script also includes some test cases to demonstrate the function's behavior.