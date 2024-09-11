```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings

    Returns:
        str: The concatenated string

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello', 'world']))  # Output: 'helloworld'
```

This Python script defines a function `concatenate` that takes a list of strings and returns a single string by concatenating all the strings in the list. The `join` method is used to concatenate the strings. The function is then tested with some example inputs to demonstrate its usage.