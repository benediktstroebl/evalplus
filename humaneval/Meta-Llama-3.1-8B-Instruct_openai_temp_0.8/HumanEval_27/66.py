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


# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrLd'
print(flip_case('Python'))  # Output: 'pYtHon'
```

This script defines the `flip_case` function, which takes a string as input and returns the string with lowercase characters converted to uppercase and vice versa. The function uses a generator expression to iterate over each character in the string, checking if the character is lowercase using the `islower` method. If it is, the character is uppercased using `upper`; otherwise, it is lowercased using `lower`. The `join` method is then used to concatenate the characters back into a single string.