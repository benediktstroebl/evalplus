```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
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
print(concatenate([]))  # Should print an empty string
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
print(concatenate(['Hello','', 'World!']))  # Should print 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation using the `join` method. It then provides some test cases to demonstrate the function's usage.