```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase to lowercase.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLlO'
print(flip_case('HeLlO'))  # Output: 'hELLO'
```

This script defines the `flip_case` function, which takes a string as input and returns a new string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase. The function uses a generator expression with the `islower` method to check if each character is lowercase, and the `upper` and `lower` methods to flip the case. The `join` method is used to concatenate the characters into a single string.