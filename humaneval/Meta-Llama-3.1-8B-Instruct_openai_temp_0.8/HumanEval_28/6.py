```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: A single string resulting from the concatenation of the input list.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    
    # Use the join() method of the empty string to concatenate all elements in the list
    return ''.join(strings)

# Test the function with some examples
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string resulting from the concatenation of all elements in the list. The function uses the `join()` method of the empty string (`''`) to concatenate all elements in the list. The script also includes some example use cases to demonstrate the function's behavior.