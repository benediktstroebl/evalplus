```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip.
    
    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase to lowercase.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

This script defines a function `flip_case` that takes a string as input, iterates over each character, checks if it's lowercase, and flips its case. The result is then returned as a string. The `islower` and `upper` methods are used to check and flip the case of each character respectively. The `join` method is used to concatenate the characters back into a string.