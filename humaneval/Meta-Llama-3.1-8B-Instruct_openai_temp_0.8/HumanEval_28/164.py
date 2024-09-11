```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: A single string that is the concatenation of all input strings.
    
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
print(concatenate(['Hello, ', 'world!']))  # Output: 'Hello, world!'
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all input strings. The `''.join(strings)` expression is used to concatenate the strings in the list. If the input list is empty, an empty string is returned.