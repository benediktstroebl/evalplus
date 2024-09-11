```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: A single string that is the concatenation of the input list.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

In this script, the `concatenate` function uses the built-in `join` method of string classes to concatenate the strings in the input list. This method is more efficient than using a loop or other methods to concatenate the strings. The `join` method takes an iterable of strings as an argument and concatenates them with the string on which it is called as a separator (in this case, an empty string).