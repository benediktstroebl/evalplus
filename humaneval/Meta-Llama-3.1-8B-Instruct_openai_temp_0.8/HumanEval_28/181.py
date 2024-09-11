```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
    strings (List[str]): A list of strings to be concatenated
    
    Returns:
    str: The concatenated string
    
    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    
    # Use the join method of the empty string to concatenate all strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print ''
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns their concatenation. It uses the `join` method of the empty string (`''`) to concatenate all strings in the list. The function is then tested with two examples.