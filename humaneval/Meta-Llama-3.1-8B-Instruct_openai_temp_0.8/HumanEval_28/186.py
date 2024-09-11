```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: A single string that is the concatenation of the input list.

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
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of the input list. The function uses the `join` method of the empty string to concatenate the strings in the list. The script also includes some example usage of the function and includes a test case for the empty list.