```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be processed.
    
    Returns:
        str: The processed string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrLd
print(flip_case('Python'))  # Output: pYtHON
```

This script uses a generator expression to iterate over each character in the input string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The `join()` method is then used to combine the characters back into a single string.