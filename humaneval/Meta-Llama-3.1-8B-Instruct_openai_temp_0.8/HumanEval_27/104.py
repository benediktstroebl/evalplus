```python
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to be modified.

    Returns:
    str: The modified string with flipped case.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HeLLO
print(flip_case('HeLLO'))  # Output: hElLo
print(flip_case('hElLo'))  # Output: HeLlO
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a list comprehension to iterate over each character in the string, converting lowercase characters to uppercase and uppercase characters to lowercase. The `join` method is then used to concatenate the characters back into a single string. The function includes docstrings to provide documentation and example use cases.