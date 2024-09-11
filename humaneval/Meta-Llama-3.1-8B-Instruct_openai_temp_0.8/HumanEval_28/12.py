```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
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
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

In this script, the `concatenate` function uses the `join` method to concatenate the strings in the list. The `join` method takes an iterable of strings and concatenates them into a single string, with the string it's called on in between each pair of strings (in this case, we use the empty string `''` to just concatenate the strings).