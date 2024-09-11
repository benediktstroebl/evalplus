```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to be concatenated

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
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. The `join` function is used to concatenate the strings in the list. The script also includes example use cases and a test in the `if __name__ == "__main__":` block to demonstrate the function's behavior.