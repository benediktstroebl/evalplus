```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The input string with case flipped.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('Python'))  # Output: 'pYTHON'
```

This script defines a function called `flip_case` that takes a string input. It uses a list comprehension to go through each character in the string, and if the character is lowercase, it converts it to uppercase. If the character is uppercase, it converts it to lowercase. The results are then joined back into a string, which is returned as the result.