### Concatenating List of Strings into a Single String

Below is a Python script that provides a function to concatenate a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
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

# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This function uses the `join()` method, which concatenates all elements in an iterable (in this case, a list of strings) into a single string. The `''` argument to `join()` means that no characters will be inserted between the concatenated strings.