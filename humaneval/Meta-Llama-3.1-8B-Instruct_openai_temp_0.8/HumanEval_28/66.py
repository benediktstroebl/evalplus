```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): List of strings to be concatenated
    
    Returns:
        str: Concatenated string
    
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
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the input list. The function uses the `join` method of the empty string (`''`), which concatenates all the strings in the input list and returns a single string. The script also includes some example use cases to demonstrate how the function works.