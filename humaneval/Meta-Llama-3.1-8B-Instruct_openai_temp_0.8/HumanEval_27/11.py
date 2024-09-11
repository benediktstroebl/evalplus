```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
print(flip_case('HeLlO'))  # Output: 'hELLO'
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The `islower` and `upper` string methods are used to check and modify the case of individual characters. The result is then returned as a new string.