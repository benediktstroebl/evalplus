```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

# Example usage:
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HELLO
```

This script defines a function `flip_case` that takes a string as input and returns the string with all uppercase characters converted to lowercase and all lowercase characters converted to uppercase. The function uses a generator expression to iterate over each character in the string, applying the `lower()` method if the character is uppercase (as determined by `isupper()`) and the `upper()` method otherwise. The resulting characters are then joined back into a string using the `''.join()` method.