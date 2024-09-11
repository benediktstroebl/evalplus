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


# Example usage:
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

In this script, the `concatenate` function takes a list of strings as input and returns their concatenation as a single string. The `join` method is used to concatenate the strings, which is a more efficient and Pythonic way to achieve this compared to using `+` operator to concatenate strings in a loop. The example usage at the end demonstrates how to use the `concatenate` function.