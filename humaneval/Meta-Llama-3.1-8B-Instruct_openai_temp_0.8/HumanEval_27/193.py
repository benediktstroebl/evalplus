```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: A new string with the case flipped.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))
print(flip_case('wOrLd'))
print(flip_case('pYtHoN'))
```

In this script, we define a function `flip_case` which takes a string as input. It uses a generator expression to iterate over each character in the string. If the character is lowercase, it converts it to uppercase using `c.upper()`. Otherwise, it converts it to lowercase using `c.lower()`. The `join` method is then used to concatenate the resulting characters into a single string. The function returns this new string.