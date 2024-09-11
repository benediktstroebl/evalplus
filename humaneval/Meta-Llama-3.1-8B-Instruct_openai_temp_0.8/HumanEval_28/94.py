### Concatenating a List of Strings into a Single String

The following Python script uses the `join()` function to concatenate a list of strings into a single string.

```markdown
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


# Test cases
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello', ', ', 'World!']))  # Output: 'Hello, World!'
```

This script defines a function `concatenate()` that takes a list of strings as input and returns a single string by joining all the strings in the list using the `join()` function. The `join()` function concatenates all the strings in the list and returns the result.

The script also includes test cases to demonstrate the usage of the `concatenate()` function.