```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Check if the input is a list
    if not isinstance(strings, list):
        raise TypeError("Input should be a list of strings")
    
    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list should be strings")
    
    # Use the join() method to concatenate the strings
    # If the list is empty, the function will return an empty string
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate()` that takes a list of strings and returns a single string concatenated from all the strings in the list. It also includes some input validation to ensure that the input is a list of strings, and raises a `TypeError` if this is not the case. The function is tested with some example cases.