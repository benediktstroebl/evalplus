```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The input string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that takes a string as input, flips its case, and returns the result. The `islower` method checks if a character is lowercase, and the `upper` and `lower` methods convert characters to uppercase and lowercase respectively. The `join` method is used to concatenate the characters in the list back into a string. The example usage at the end shows how to use the function.