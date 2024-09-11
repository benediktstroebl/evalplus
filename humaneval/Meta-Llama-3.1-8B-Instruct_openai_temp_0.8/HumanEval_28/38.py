```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
    strings (List[str]): A list of strings to be concatenated.
    
    Returns:
    str: A single string that is the concatenation of all strings in the input list.
    
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
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
print(concatenate(['1', '2', '3']))  # Output: '123'
```

In this script, the `concatenate` function uses the `''.join(strings)` method to concatenate all strings in the input list into a single string. The `join` method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings. Since we're calling `''.join(strings)`, it concatenates all strings in `strings` without any extra characters in between.