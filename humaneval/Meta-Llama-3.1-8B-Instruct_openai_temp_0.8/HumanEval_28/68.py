```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings

    Returns:
    str: A single string concated from all strings in the list

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Check if the input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")

    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list must be strings")

    # Convert the list to a string joined by an empty string
    # This effectively concatenates all strings in the list
    concatenated = ''.join(strings)

    return concatenated

# Example usage
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```