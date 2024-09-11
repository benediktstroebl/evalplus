```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
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
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```

In this script, the `flip_case` function iterates over each character in the input string. If the character is lowercase (`c.islower()` returns `True`), it converts it to uppercase (`c.upper()`). Otherwise, it converts it to lowercase (`c.lower()`). The function then returns the resulting string.