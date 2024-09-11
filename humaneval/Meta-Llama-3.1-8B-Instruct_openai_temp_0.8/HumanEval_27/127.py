```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('Hello World'))  # Output: hELLO wORLD
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. The function uses a generator expression to iterate over each character in the string, converting it to uppercase if it was lowercase and vice versa using the `islower` and `upper`/`lower` methods. The `join` method is then used to concatenate the characters back into a string.