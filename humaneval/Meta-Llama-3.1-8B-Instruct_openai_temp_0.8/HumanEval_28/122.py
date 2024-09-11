```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the result of concatenating all strings in the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello ', 'World!']))  # Output: 'Hello World!'
```

In this script, we define a function `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all strings in the list. The `join` method is used to concatenate the strings. If the input list is empty, an empty string is returned.