```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HeLLO
print(flip_case('123abc'))  # Output: 123ABC
```

This script defines a function called `flip_case` which takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function uses a list comprehension to iterate over each character in the string, converting it to uppercase if it's lowercase and vice versa. The resulting list of characters is then joined back into a string.