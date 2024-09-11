```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrld
```

This script uses a generator expression to iterate over each character in the input string. The `islower()` method checks if a character is lowercase, and if so, it's converted to uppercase with `upper()`. Otherwise, it's converted to lowercase with `lower()`. Finally, the `join()` method concatenates the characters back into a string.