### Flip Case of a String
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```
This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a generator expression with the `join` method to efficiently create the resulting string. The `islower` method checks if a character is lowercase, and the `upper` and `lower` methods are used to flip the case of each character.