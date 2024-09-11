```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the result of concatenating the input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join method of the empty string to concatenate the list of strings
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all the strings in the list. The `join` method is used to concatenate the strings, which is a more efficient and Pythonic way to do this than using the `+` operator to concatenate the strings one by one. The script also includes some example use cases to test the function.