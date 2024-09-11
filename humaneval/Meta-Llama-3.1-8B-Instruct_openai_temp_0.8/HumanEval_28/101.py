```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Check if input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")
    
    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list must be strings.")
    
    # Use the join() method to concatenate the strings
    return ''.join(strings)

# Example usage:
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate([]))  # Output: ''
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate()` that takes a list of strings as input and returns their concatenation as a single string. The function includes error checking to ensure that the input is a list and that all elements in the list are strings. If the input is not valid, the function raises a `TypeError`.