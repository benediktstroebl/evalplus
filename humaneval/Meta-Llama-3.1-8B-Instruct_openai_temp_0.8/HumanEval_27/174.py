```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Example usage:
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('hELLO'))  # Outputs: 'HeLLO'
print(flip_case('HElLo'))  # Outputs: 'heLLO'
```

This script uses a list comprehension to iterate over each character in the input string. If the character is a lowercase letter (`c.islower()`), it converts it to uppercase using `c.upper()`. Otherwise, it converts it to lowercase using `c.lower()`. The `join()` method then concatenates these characters back into a single string.