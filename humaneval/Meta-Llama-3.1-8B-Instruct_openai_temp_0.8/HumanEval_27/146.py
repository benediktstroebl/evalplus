```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('WORLD'))  # Outputs: 'wOrld'
```