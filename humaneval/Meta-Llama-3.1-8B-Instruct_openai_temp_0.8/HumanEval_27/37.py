```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be modified.
    
    Returns:
        str: The modified string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. The function uses a generator expression to iterate over each character in the string. If the character is lowercase, it is converted to uppercase, and if it is uppercase, it is converted to lowercase. The `join` function is then used to concatenate the modified characters back into a string. The script also includes a test case to demonstrate the function's behavior.