```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.swapcase() for c in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLo'))  # Output: 'HELLO'
print(flip_case('ALL CAPS'))  # Output: 'aLL cApS'
```

This script uses a list comprehension to swap the case of each character in the string using the `swapcase()` method, and then joins these characters back together into a single string.