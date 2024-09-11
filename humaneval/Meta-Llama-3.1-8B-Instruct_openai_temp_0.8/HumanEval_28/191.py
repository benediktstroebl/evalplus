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


# Test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string by concatenating all the input strings together. The `join` method is used with an empty string (`''`) as the separator to concatenate all the strings without any spaces in between. The script also includes some test cases to demonstrate the function's behavior.