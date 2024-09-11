```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string that is the concatenation of all input strings

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join() function with an empty string to concatenate all strings
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate(['Hello','', 'World']))  # Expected output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of all input strings. The function uses the `join()` method to concatenate the strings. The test cases at the end demonstrate the function's behavior with an empty list, a list of single characters, and a list of words.