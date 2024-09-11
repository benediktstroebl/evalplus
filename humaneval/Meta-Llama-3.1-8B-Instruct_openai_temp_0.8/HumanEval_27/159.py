```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case(''))  # Output: ''
```

This script defines a function `flip_case` that takes a string as input and returns a string where all lowercase characters are flipped to uppercase and vice versa. It uses a list comprehension to iterate over each character in the string, checking whether it's lowercase using the `islower` method, and applying the `upper` or `lower` method accordingly. The resulting characters are then joined back into a string using the `join` method.