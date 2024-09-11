### Concatenating a List of Strings into a Single String

Here's a self-contained Python script that defines a function `concatenate` to concatenate a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string after concatenating all elements in the input list

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

This script defines the `concatenate` function, which uses the `''.join()` method to concatenate all strings in the input list into a single string. If the input list is empty, it returns an empty string. You can test the function with different inputs as shown in the example usage section.