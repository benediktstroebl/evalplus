```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated
    
    Returns:
        str: A single string resulting from concatenation of all input strings
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method concatenates all the strings in the list and returns a single string
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string resulting from concatenation of all input strings. The function uses the `join()` method to concatenate all strings in the list. The script also includes test cases to verify the function's behavior.