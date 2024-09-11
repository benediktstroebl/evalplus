### Flip Case of a String
#### Python Script

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
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Example usage
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```

In this script, the `flip_case` function uses a list comprehension to iterate over each character in the input string. If the character is lowercase (`islower()` returns `True`), it is converted to uppercase using `upper()`. Otherwise, the character is converted to lowercase using `lower()`. The resulting characters are then joined back into a string using `''.join()`.