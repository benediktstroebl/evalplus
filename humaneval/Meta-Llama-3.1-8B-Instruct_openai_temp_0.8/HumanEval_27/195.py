```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string
    
    Returns:
    str: The string with lowercase characters converted to uppercase and uppercase characters converted to lowercase.
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('aBcDe'))  # Output: 'aBcDe'
```

This script defines a function `flip_case` that takes a string as input, and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. It uses a generator expression to achieve this in a concise and efficient way. The test cases at the end of the script demonstrate the function's behavior.