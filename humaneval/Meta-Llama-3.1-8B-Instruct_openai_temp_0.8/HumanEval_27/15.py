```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with case flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLLO'
print(flip_case('HeLLO'))  # Output: 'hELOO'
```

This script uses a generator expression to iterate over each character `c` in the input `string`. The `islower()` method is used to check if a character is lowercase, and the `upper()` method is used to flip it to uppercase. The `join()` method is then used to concatenate the flipped characters back into a string.