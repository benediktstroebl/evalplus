```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to flip case.
    
    Returns:
    str: The string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase.
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
print(flip_case('HeLlO'))  # Output: 'hELLO'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with all its characters' cases flipped. It uses a list comprehension to iterate over each character in the string, converting uppercase characters to lowercase and vice versa, and then joins these characters back into a string. The function is then tested with a few examples to demonstrate its usage.