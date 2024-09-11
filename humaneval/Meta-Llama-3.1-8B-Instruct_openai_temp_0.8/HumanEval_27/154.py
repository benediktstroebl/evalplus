```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)


# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLLO'
print(flip_case('HeLLO'))  # Output: 'hElLo'
print(flip_case('hElLo'))  # Output: 'hELLO'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The `islower` and `upper` methods of Python strings are used to check and modify the case of individual characters, respectively. The `''.join()` method is used to concatenate the modified characters into a single string.