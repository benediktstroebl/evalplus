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
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
print(flip_case('123abc'))
```

This script defines a function `flip_case` that takes a string as input, iterates over each character in the string, and checks if the character is lowercase using the `islower()` method. If the character is lowercase, it converts it to uppercase using the `upper()` method; otherwise, it converts it to lowercase using the `lower()` method. The resulting characters are then joined together using the `join()` method to form the final string with flipped case.