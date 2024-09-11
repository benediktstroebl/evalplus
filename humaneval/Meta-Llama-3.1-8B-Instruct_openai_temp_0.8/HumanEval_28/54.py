```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
    strings (List[str]): List of strings to be concatenated
    
    Returns:
    str: The concatenated string
    
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    if not strings:  # Check if the list is empty
        return ''  # If empty, return an empty string
    return ''.join(strings)  # Use join method to concatenate strings


# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings `strings` and returns their concatenation. If the input list is empty, it returns an empty string. Otherwise, it uses the `join` method to concatenate all strings in the list.