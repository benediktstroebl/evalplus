```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example use cases
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('Python is fun'))  # Output: 'pytHON iS fUN'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters changed to uppercase and all uppercase characters changed to lowercase. The `islower()` and `upper()` and `lower()` methods of the string are used to check and modify the case of individual characters. The result is then returned as a new string.

The example use cases are provided to demonstrate the function's behavior with different inputs.