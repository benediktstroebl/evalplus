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
    # Use the join method of the string class to concatenate the list of strings
    # The join method returns a string in which the elements of the list have been joined by the string on which the method was called
    # In this case, we use the empty string '' to join the elements of the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the list. The function uses the `join` method of the string class to concatenate the list of strings. The script also includes some test cases to demonstrate the function's behavior.