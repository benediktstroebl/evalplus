### Flip Case Function in Python

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
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test the function
print(flip_case('Hello'))  # Outputs: hELLO
print(flip_case('hello'))  # Outputs: HELLO
print(flip_case('HeLlO'))  # Outputs: hElLo
```

This script defines a function called `flip_case` that takes a string as input and returns a new string with the case of each character flipped. It uses a list comprehension to iterate over each character in the string, checks if the character is uppercase using the `isupper` method, and uses the `lower` or `upper` method to flip its case. The resulting list of characters is then joined back together into a string using the `''.join()` method.