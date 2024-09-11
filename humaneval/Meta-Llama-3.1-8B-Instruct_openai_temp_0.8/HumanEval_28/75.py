```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Testing the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello, ', 'world!']))  # Output: 'Hello, world!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation. The function uses the `join` method of the empty string, which concatenates all the strings in the list into a single string. The script also includes some test cases to demonstrate the function's behavior.