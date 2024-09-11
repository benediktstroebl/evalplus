```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip case.
    
    Returns:
        str: The input string with flipped case.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('aBc'))    # Output: 'AbC'
```

This script uses a generator expression to iterate over each character in the string. For each character, it checks if the character is lowercase using the `islower()` method. If it's lowercase, it converts it to uppercase with `upper()`. Otherwise, it leaves it as is. The `join()` method is then used to concatenate all the characters back into a single string.