```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Args:
        string (str): The input string to flip case

    Returns:
        str: The string with characters flipped

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This Python script defines a function `flip_case` that takes a string as input and returns the string with characters flipped from lowercase to uppercase and vice versa. The function uses a list comprehension to iterate over each character in the string, and if the character is lowercase, it is converted to uppercase, otherwise it is converted to lowercase. The `join` function is then used to concatenate the characters back into a string. The script also includes some example usage to demonstrate the function's behavior.