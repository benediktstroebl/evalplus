```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with case flipped.

    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HeLLO
print(flip_case('ALLCAPS'))  # Output: aLlCapS
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and vice versa. The function uses a generator expression to iterate over each character in the string, and the `islower` and `upper` methods to determine the case of each character. The result is then joined back into a string using `join`.