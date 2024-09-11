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
    # Use the join function to concatenate the strings in the list
    # The join function takes an iterable of strings and concatenates them with the string it is called on
    # Since we want an empty string between the concatenated strings, we call join on an empty string
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the input list. The `join` function is used to concatenate the strings. The script also includes some example use cases to demonstrate how the function works.