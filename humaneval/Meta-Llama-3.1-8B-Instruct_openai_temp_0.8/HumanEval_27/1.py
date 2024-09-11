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
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('HelloWorld'))  # Output: 'hELLOwORLD'
```

This script defines a function `flip_case` that uses a generator expression to iterate over each character `c` in the input string. If `c` is a lowercase letter (`islower()` returns `True`), it converts it to uppercase using `c.upper()`. Otherwise, it converts it to lowercase using `c.lower()`. The resulting characters are then joined into a new string using `''.join()`.