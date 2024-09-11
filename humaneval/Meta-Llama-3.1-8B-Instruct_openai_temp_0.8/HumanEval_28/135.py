```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings
    
    Returns:
        str: The concatenated string
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Example usage:
print(concatenate([]))   # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','world']))  # Output: 'hello world'
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation. The `join` method is used to concatenate the strings, and example usage is provided at the end of the script.