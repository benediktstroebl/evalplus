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


# Example usage:
if __name__ == "__main__":
    print(concatenate([]))     # Output: ''
    print(concatenate(['a', 'b', 'c']))     # Output: 'abc'
    print(concatenate(['Hello, ', 'World!']))     # Output: 'Hello, World!'
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation. It uses the `join` method of a string, which concatenates all the strings in the list with no separator. The script also includes example usage to demonstrate how to use the function.