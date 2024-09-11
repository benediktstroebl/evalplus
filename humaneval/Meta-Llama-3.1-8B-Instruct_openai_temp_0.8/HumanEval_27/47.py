```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to be flipped.

    Returns:
    str: The resulting string with flipped case.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)


# Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # Expected output: hELLO
    print(flip_case('WORLD'))  # Expected output: wOrld
```

This script defines a function `flip_case` that takes a string as input, iterates over each character, and applies the opposite case operation using the `isupper()` and `lower()` methods for uppercase characters, and `isupper()` and `upper()` methods for lowercase characters. The resulting characters are then joined back into a string and returned.