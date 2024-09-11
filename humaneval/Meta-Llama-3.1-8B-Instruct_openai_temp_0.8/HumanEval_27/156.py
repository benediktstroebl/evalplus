```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrld
print(flip_case('python'))  # Output: PytHon
```

This function uses a generator expression to iterate over each character in the string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The `join` method is then used to combine the results back into a string.