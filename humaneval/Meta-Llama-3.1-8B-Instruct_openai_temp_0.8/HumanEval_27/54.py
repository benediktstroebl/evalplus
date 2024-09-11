```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be flipped.
    
    Returns:
        str: The input string with flipped case.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(
        char.upper() if char.islower() 
        else char.lower() 
        for char in string
    )

# Test the function
print(flip_case('Hello'))
print(flip_case('WORLD'))
print(flip_case('123ab'))
```

This Python script defines a function called `flip_case` that takes a string as input and returns the string with its case flipped. The function uses a generator expression to iterate over each character in the input string. If a character is lowercase, it's converted to uppercase; otherwise, it's converted to lowercase. The `join` method is used to concatenate the characters back into a string.