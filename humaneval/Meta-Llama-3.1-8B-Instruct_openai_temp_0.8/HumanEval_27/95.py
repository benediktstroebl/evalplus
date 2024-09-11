### Flip Case Function in Python
#### Description
This script defines a function `flip_case` that takes a string as input and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase.

```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
```

This function uses a generator expression to iterate over each character `c` in the input string. If the character is lowercase (checked using `c.islower()`), it is converted to uppercase using `c.upper()`. Otherwise, it is converted to lowercase using `c.lower()`. The resulting characters are then joined back together into a string using `''.join(...)`.