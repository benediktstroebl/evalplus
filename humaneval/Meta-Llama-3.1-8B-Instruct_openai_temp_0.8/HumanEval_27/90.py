```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with characters flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'world'
```

In this code, `swapcase()` is a string method that returns the characters of the string in uppercase if they are lowercase, and vice versa. We use a generator expression to apply this method to each character in the string, and then join the resulting characters back into a string.