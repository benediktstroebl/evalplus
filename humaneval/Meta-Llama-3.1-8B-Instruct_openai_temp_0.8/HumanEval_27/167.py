```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with flipped case.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('A B C'))  # Output: 'a b c'
```

This script defines a function `flip_case` that takes a string as input, flips the case of each character, and returns the resulting string. The `islower` and `upper` methods are used to check the case of each character and to convert it to the opposite case, respectively. The `join` method is used to concatenate the characters into a single string.