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


# Example use cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```

In this script, the `concatenate` function uses the built-in `join` method of Python strings to concatenate all the strings in the input list. If the input list is empty, it returns an empty string.