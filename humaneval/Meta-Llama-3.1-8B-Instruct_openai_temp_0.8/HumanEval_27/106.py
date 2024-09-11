### Flip Case Function
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to flip case.

    Returns:
    str: The input string with flipped case.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
print(flip_case('aBc'))    # Output: 'AbC'
```
This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a generator expression to iterate over each character in the string, converting lowercase characters to uppercase and uppercase characters to lowercase using the `islower()` and `upper()` methods. The resulting characters are then joined back into a string using the `''.join()` method. The script includes example use cases to demonstrate the function's behavior.