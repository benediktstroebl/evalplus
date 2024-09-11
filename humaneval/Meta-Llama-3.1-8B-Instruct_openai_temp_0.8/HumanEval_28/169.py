```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string that is the result of concatenating all the input strings

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Using the join() method to concatenate all strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function called `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all the input strings. The function uses the `join()` method, which is a built-in method of the string class in Python, to concatenate all the strings in the list. If the input list is empty, the function returns an empty string.