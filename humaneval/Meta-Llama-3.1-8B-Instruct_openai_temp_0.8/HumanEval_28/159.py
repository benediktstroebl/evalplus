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
        # concatenate the current string to the result
        result += string

    # Return the final concatenated string
    return result

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

Note that Python has a built-in string method `join()` that can be used to concatenate a list of strings in a more efficient and concise way:

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
    # Use the join() method to concatenate the strings
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This version of the function achieves the same result but is much more concise and efficient.