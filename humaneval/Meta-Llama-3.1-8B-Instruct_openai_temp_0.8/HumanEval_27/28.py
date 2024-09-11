```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be processed.
    
    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test the function
print(flip_case('Hello'))
print(flip_case('WORLD'))
print(flip_case(''))
```

In this script, we use a list comprehension to iterate over each character in the string. If a character is uppercase (checked using `char.isupper()`), we convert it to lowercase using `char.lower()`. If a character is lowercase (implicitly true since `char.isupper()` is false), we convert it to uppercase using `char.upper()`. The resulting characters are then joined together into a single string using the `join()` method.