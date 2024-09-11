```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

This script uses a list comprehension to iterate over each character in the string, converting lowercase characters to uppercase and uppercase characters to lowercase using the `islower()` and `upper()` methods. The `join()` method is then used to concatenate all the characters back into a single string.