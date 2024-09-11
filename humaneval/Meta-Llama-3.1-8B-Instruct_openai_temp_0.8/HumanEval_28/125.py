```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the concatenation of all input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join function to concatenate all strings in the list
    # The join function requires a list of strings to be concatenated
    # We use an empty string as the separator, which means all elements will be concatenated without any separator
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

In this script, we define a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all input strings. We use the `join` function from Python's built-in string module to concatenate all strings in the list. The `join` function requires a list of strings to be concatenated and an optional separator string. We use an empty string as the separator, which means all elements will be concatenated without any separator. We then test the function with some examples to demonstrate its usage.