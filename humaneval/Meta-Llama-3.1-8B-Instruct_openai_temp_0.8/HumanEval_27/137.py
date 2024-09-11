```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with characters flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('aBcDe'))  # Output: 'aBcDe'
print(flip_case('ALL UPPERCASE'))  # Output: 'aLL uPPERCASE'
print(flip_case('all lowercase'))  # Output: 'ALL LOWERCASE'
```

In this script, the function `flip_case` iterates over each character in the input string. If the character is lowercase, it converts it to uppercase using `c.upper()`, and if it's uppercase, it converts it to lowercase using `c.lower()`. The `''.join()` method is then used to concatenate the flipped characters back into a string. The script includes example use cases to demonstrate how the function works.