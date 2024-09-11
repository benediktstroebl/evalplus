```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to concatenate

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
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

In this script, we define a function called `concatenate` that takes a list of strings as input. We then use the `join` method on an empty string ('') to concatenate all the strings in the list into a single string. This method is a more efficient and elegant way to concatenate strings in Python compared to using the `+` operator.