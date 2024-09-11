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
    # Use the join method of the empty string to concatenate all elements in the list
    return ''.join(strings)


# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string by concatenating all the elements in the list. It uses the `join` method of the empty string to achieve this. The example usage at the end demonstrates how to use this function.