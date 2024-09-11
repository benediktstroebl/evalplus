### Concatenating List of Strings into a Single String
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string containing all the strings from the input list.

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))   # Output: ''
print(concatenate(['a', 'b', 'c']))   # Output: 'abc'
print(concatenate(['Hello','', 'World', '!']))   # Output: 'Hello World!'
```
This script defines a function `concatenate` that takes a list of strings as input and returns a single string containing all the strings from the input list. The function uses the `join` method of the empty string, which concatenates all the strings in the list into a single string. The `join` method is more efficient and Pythonic than using the `+` operator to concatenate strings.