```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to be flipped.
    
    Returns:
    str: The string with cases flipped.
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
print(flip_case('WORLD'))  # Output: world
print(flip_case('world'))  # Output: WORLD
```

This script defines a function `flip_case` that takes a string as input and returns the string with its cases flipped. The function uses a generator expression to iterate over each character in the string, flipping its case if it's lowercase (converting to uppercase) or uppercase (converting to lowercase). The resulting string is then returned.

The script also includes some example use cases to demonstrate the function's behavior.