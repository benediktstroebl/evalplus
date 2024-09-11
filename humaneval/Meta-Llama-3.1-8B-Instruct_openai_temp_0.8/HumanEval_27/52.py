```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be modified.
    
    Returns:
        str: The string with characters flipped.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

# Test the function
print(flip_case('Hello'))
print(flip_case('WORLD'))
print(flip_case('Python'))
```

This script defines a function `flip_case` that takes a string as input and returns the string with lowercase characters converted to uppercase and vice versa. It uses a simple loop to iterate over each character in the string, checking if it's lowercase or uppercase using the `islower` method. If it's lowercase, it converts it to uppercase using the `upper` method; if it's uppercase, it converts it to lowercase using the `lower` method.