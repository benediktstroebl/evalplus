```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the result of the concatenation.

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
print(concatenate(['Hello','', 'World']))  # Output:'Hello World'
```

In this script, we define a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. The function uses the `join` method of the empty string (`''`) to concatenate the input strings. We also include some example use cases to demonstrate the function's behavior.