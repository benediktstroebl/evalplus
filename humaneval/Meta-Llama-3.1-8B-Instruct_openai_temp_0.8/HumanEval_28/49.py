### Concatenating List of Strings into a Single String
#### Problem Description
This script defines a function `concatenate` that takes a list of strings and returns a single string formed by concatenating all the strings in the list.

#### Code
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string formed by concatenating all the strings in the list

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Example usage
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

#### Explanation
The `concatenate` function uses the built-in `join` method of Python's string class. This method takes an iterable as an argument, concatenates all the strings in the iterable, and returns the result. Since the `join` method is called on an empty string (`''`), it concatenates all the strings in the list without any separator in between.

This approach is more efficient than using the `+` operator to concatenate strings because it avoids creating intermediate strings and thus reduces memory usage and computation time.