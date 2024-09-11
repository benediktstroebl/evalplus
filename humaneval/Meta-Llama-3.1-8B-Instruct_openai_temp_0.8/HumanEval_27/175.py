### Flip Case String Function
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to flip case.

    Returns:
    str: The string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

### Example Use Cases
```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
print(flip_case('HeLlO'))  # Output: 'HeLlO'
```
This script defines a function `flip_case` that takes a string as input and returns a new string with the case flipped. It uses a generator expression to iterate over each character `c` in the input string. If `c` is lowercase, it converts it to uppercase using `c.upper()`, otherwise it converts it to lowercase using `c.lower()`. The resulting characters are then joined together using `''.join()` to form the final output string.