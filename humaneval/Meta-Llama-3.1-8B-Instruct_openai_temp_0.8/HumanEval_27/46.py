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
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('WORLD'))  # Outputs: 'wOrLd'
print(flip_case('Python'))  # Outputs: 'pYtHoN'
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. The function uses a generator expression to iterate over each character in the string, and for each character, it uses the `islower` method to determine if it's lowercase. If it is, it's converted to uppercase using the `upper` method. Otherwise, it's converted to lowercase using the `lower` method. The resulting characters are then joined together into a single string using the `join` method.