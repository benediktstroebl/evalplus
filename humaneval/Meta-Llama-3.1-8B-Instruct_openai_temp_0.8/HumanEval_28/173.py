```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

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
if __name__ == '__main__':
    print(concatenate([]))       # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

In this script, the `concatenate` function takes a list of strings as input and uses the `join` method to concatenate them into a single string. The function is well-documented with a docstring that includes a description, input and output parameters, and examples of usage. The code also includes example usage at the end to demonstrate how to use the `concatenate` function.