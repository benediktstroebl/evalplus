```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
    strings (List[str]): A list of strings to be concatenated.
    
    Returns:
    str: The concatenated string.
    
    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Example usage
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```

This script uses the built-in `join()` function, which is a more efficient and Pythonic way to concatenate strings than using the `+` operator in a loop. The `join()` function takes an iterable of strings and joins them together with the string it's called on in between each pair of strings. If the string is an empty string, as in this case, it effectively concatenates the strings without any separator.