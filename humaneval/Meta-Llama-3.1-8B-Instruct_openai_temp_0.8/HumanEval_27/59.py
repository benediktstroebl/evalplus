```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that uses a list comprehension to iterate over each character in the input string. The `swapcase` method is used to flip the case of each character, and the resulting list of characters is joined back into a string using the `join` method. The script also includes a test case to demonstrate the function's behavior.