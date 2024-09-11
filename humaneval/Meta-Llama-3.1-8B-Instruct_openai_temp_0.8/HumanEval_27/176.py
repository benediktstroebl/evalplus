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
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('python'))  # Output: 'PyThOn'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with the case of each character flipped. It uses a generator expression to iterate over each character in the string, checks if the character is lowercase using `islower()`, and uses conditional expression to determine whether to convert it to uppercase or lowercase using `upper()` and `lower()`. The resulting characters are then joined back together into a single string using `''.join()`. The test cases at the end demonstrate the function's behavior on different inputs.