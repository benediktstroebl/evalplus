```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the result of concatenating all input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Initialize an empty string to store the concatenated result
    result = ''

    # Iterate over each string in the input list
    for string in strings:
        # Concatenate the current string to the result
        result += string

    # Return the final concatenated string
    return result

# Example usage:
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate([]))  # Output: ''
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the result of concatenating all the input strings. It uses a for loop to iterate over each string in the input list and concatenates each string to the result using the `+=` operator. The function includes docstrings to explain its purpose, usage, and expected input and output.