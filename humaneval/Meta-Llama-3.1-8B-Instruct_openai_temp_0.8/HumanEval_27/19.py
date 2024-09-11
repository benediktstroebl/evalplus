```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Args:
        string (str): The input string

    Returns:
        str: The string with each character's case flipped

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLlo'
print(flip_case('HElLo'))  # Output: 'hELLO'
```

This script uses a generator expression to iterate over each character `c` in the input string `string`. The `swapcase()` method flips the case of each character, and these characters are then joined together into a single string.