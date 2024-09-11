### Concatenating List of Strings into a Single String
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from concatenating all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Expected output: 'Hello World!'
```
This Python script defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. It uses the built-in `join` method of the empty string '', which concatenates all strings in the input list without any separator.

The test cases at the end demonstrate the function's behavior with an empty list, a list of three characters, and a list of three words with spaces in between.