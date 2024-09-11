```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from concatenating all strings in the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

In this script, the `concatenate` function uses Python's built-in string method `join()`, which concatenates all strings in the input list `strings` into a single string. If the input list is empty, an empty string is returned, as per the problem's requirements. The example usage demonstrates the function's behavior with different input lists.