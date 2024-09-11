```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with all characters flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The resulting list of characters is then joined back together into a single string. The `islower()` method checks if a character is lowercase, and the `upper()` and `lower()` methods are used to convert characters to uppercase and lowercase, respectively.