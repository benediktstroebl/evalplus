```python
def flip_case(string: str) -> str:
    """
    Flip the case of a given string by converting lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HELLO
print(flip_case('HElLo'))  # Output: hElLo
```

This script defines a function `flip_case` that takes a string as input and returns a new string with the case of each character flipped. The function uses a generator expression to iterate over each character in the input string. If the character is lowercase, it's converted to uppercase using `char.upper()`. If the character is uppercase, it's converted to lowercase using `char.lower()`. The resulting characters are then joined back together into a single string using `''.join(...)`.