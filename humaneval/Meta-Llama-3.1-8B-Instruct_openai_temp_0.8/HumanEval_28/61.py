```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): The list of strings to be concatenated.
    
    Returns:
        str: The concatenated string.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate the strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. It uses the built-in `join()` method of the string class to concatenate the strings. The test at the end demonstrates the function's behavior with both an empty list and a list with three strings.